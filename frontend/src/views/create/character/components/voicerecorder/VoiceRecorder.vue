<script setup>
import {onBeforeUnmount, ref} from "vue"
import api from "@/js/http/api"
import {useUserStore} from "@/stores/user.js"

const user = useUserStore()

let mediaRecorder = null
let audioChunks = []
let stream = null

const recording = ref(false)
const loading = ref(false)
const errorMessage = ref('')

const emit = defineEmits(["success"])

let timer = null

// 录音
const startRecord = async () => {
  try {
    stream = await navigator.mediaDevices.getUserMedia({audio: true})
    mediaRecorder = new MediaRecorder(stream)
    audioChunks = []

    mediaRecorder.ondataavailable = (e) => {
      audioChunks.push(e.data)
    }

    mediaRecorder.onstop = async () => {
      const blob = new Blob(audioChunks, {type: "audio/webm"})
      blob.name = "record.webm"
      await upload(blob)
    }

    mediaRecorder.start()
    recording.value = true

    // 30秒自动停止
    timer = setTimeout(() => {
      stopRecord()
    }, 30000)

  } catch (e) {
    errorMessage.value = "无法访问麦克风"
  }
}

const stopRecord = () => {
  try {
    if (mediaRecorder && recording.value) {
      mediaRecorder.stop()
    }
  } catch (e) {}

  if (stream) {
    stream.getTracks().forEach(track => track.stop())
    stream = null
  }

  if (timer) {
    clearTimeout(timer)
    timer = null
  }

  recording.value = false
}

// 文件上传
const handleFileUpload = async (e) => {
  const file = e.target.files[0]
  if (!file) return

  if (!file.type.startsWith("audio/")) {
    errorMessage.value = "请上传音频文件"
    return
  }

  await upload(file)
}

const upload = async (file) => {
  loading.value = true
  errorMessage.value = ''

  const formData = new FormData()
  formData.append("audio", file, file.name || "voice.webm")
  formData.append("name", user.username)

  try {
    const res = await api.post("/api/create/character/voice/clone_voice/", formData)
    const data = res.data

    if (data.result === "success") {
      emit("success", data.voice)
    } else {
      errorMessage.value = data.result
    }

  } catch (e) {
    console.error(e)
    errorMessage.value = "上传失败"
  } finally {
    loading.value = false
  }
}

onBeforeUnmount(() => {
  stopRecord()
})
</script>

<template>
  <div class="mt-2">
    <div class="text-xs text-gray-400">
      请朗读一段清晰语音（5~10秒）
    </div>

    <div class="flex gap-2 mt-2">

      <button
          class="btn btn-sm btn-primary"
          @click="startRecord"
          :disabled="recording"
      >
        🎤 录音
      </button>

      <button
          class="btn btn-sm btn-error"
          @click="stopRecord"
          :disabled="!recording"
      >
        ⏹ 停止
      </button>

      <label class="btn btn-sm">
        📁 上传
        <input
            type="file"
            hidden
            accept="audio/*"
            @change="handleFileUpload"
        />
      </label>

    </div>

    <div v-if="errorMessage" class="text-red-500 text-sm mt-1">
      {{ errorMessage }}
    </div>

    <div v-if="loading" class="text-sm text-gray-500 mt-1">
      正在生成音色...
    </div>
  </div>
</template>

<style scoped>
</style>
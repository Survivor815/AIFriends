<script setup>
import {onBeforeUnmount, ref} from "vue"
import api from "@/js/http/api"
import {useRoute} from "vue-router";
import {useUserStore} from "@/stores/user.js";
const user=useUserStore()

let mediaRecorder = null
let audioChunks = []
let stream = null   // 保存麦克风流
const recording = ref(false)
const loading = ref(false)
const errorMessage=ref('')
const emit = defineEmits(["success"])

let timer = null
const startRecord = async () => {
  stream = await navigator.mediaDevices.getUserMedia({audio: true})
  mediaRecorder = new MediaRecorder(stream)
  audioChunks = []

  mediaRecorder.ondataavailable = (e) => {
    audioChunks.push(e.data)
  }

  mediaRecorder.onstop = async () => {
    const blob = new Blob(audioChunks, {type: "audio/webm"})
    await upload(blob)
  }

  mediaRecorder.start()
  recording.value = true

  // ⭐ 30秒自动停止
   timer = setTimeout(() => {
    stopRecord()
  }, 30000)
}

const stopRecord = () => {
   try {
    if (mediaRecorder && recording.value) {
      mediaRecorder.stop()
    }
  } catch (e) {
    console.warn("stop error:", e)
  }

   if (stream) {
    stream.getTracks().forEach(track => track.stop())
    stream = null
  }
   // 停止时清除定时器
   if (timer) {
    clearTimeout(timer)
    timer = null
  }
   recording.value = false
}

const upload = async (blob) => {
  loading.value = true
  const formData = new FormData()
  formData.append("audio", blob, "voice.webm")
  formData.append("name", user.username)

  try {
    const res = await api.post("/api/create/character/voice/clone_voice/", formData)
    const data = res.data
    if (data.result === "success") {
      emit("success", data.voice)
    }else {
      errorMessage.value=data.result
    }
  } catch (e) {
    console.error(e)
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
    <div class="flex gap-2">
      <button
          class="btn btn-sm btn-primary"
          @click="startRecord"
          :disabled="recording"
      >
        🎤 开始录音
      </button>

      <button
          class="btn btn-sm btn-error"
          @click="stopRecord"
          :disabled="!recording"
      >
        ⏹ 停止
      </button>
    </div>
   <div v-if="errorMessage">{{errorMessage}}</div>
    <div v-if="loading" class="text-sm text-gray-500 mt-1">
      正在生成音色...
    </div>
  </div>
</template>

<style scoped>

</style>
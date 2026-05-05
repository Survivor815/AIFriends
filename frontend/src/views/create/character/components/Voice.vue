<script setup>
import {ref, watch} from "vue";
import VoiceRecorder from "@/views/create/character/components/voicerecorder/VoiceRecorder.vue";

const props=defineProps(['voices','curVoiceId',''])
const emit = defineEmits(["refresh"])
const myVoice = ref(props.curVoiceId)

watch(() => props.curVoiceId, newVal => {
  myVoice.value = newVal
})

const handleNewVoice = (voice) => {
  // 通知父组件刷新列表
  emit("refresh", voice)
}

defineExpose({
  myVoice,
})
</script>

<template>
  <fieldset class="fieldset">
    <label class="label text-base">音色</label>
    <select v-model="myVoice" class="select">
      <option
          v-for="voice in voices"
          :id="voice.id"
          :value="voice.id"
      >{{ voice.name }}</option>
    </select>
    <VoiceRecorder @success="handleNewVoice" />
  </fieldset>
</template>

<style scoped>

</style>

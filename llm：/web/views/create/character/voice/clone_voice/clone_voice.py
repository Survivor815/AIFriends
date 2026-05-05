import os
import traceback
import uuid

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from backend import settings
from web.models.character import Voice
from web.views.create.character.voice.custom.create_voice import create_voice
class CloneVoiceView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            audio=request.FILES['audio']
            name=request.data.get('name',"voice")

            if not audio:
                return Response({
                    'result': '语音为空，请重试',
                })
            #保存语音
            file_name = f"{uuid.uuid4().hex}.mp3"
            file_path = os.path.join(settings.MEDIA_ROOT, "tmp", file_name)
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            with open(file_path,'wb') as f:
                for chunk in audio.chunks():
                    f.write(chunk)

            voice_url = f"{settings.MEDIA_URL}tmp/{file_name}"
            res=create_voice(voice_url,prefix=str(name))
            voice_id=res.get("output",{}).get("voice_id")
            if not voice_id:
                return Response({
                    'result':"复刻语音失败",
                    'detail':res
                })
            voice_obj=Voice.objects.create(
                name=name,
                voice_id=voice_id
            )
            os.remove(file_path)
            return Response({
                'result':"success",
                'voice':{
                    "id":voice_obj.id,
                    "name":voice_obj.name
                }
            })
        except Exception as e:
            traceback.print_exc()
            return Response({
                'result': '系统异常，请稍后重试',
                'detail': str(e)
            })
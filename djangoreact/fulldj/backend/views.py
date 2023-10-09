from django.shortcuts import render
from rest_framework.views import APIView
from .models import Video
from .serializer import VideoSerializer
from rest_framework.response import Response
# Create your views here.

class VideoView(APIView):
    def get(self,request):
        output = [
            {
                "title": output.title,
                "channel": output.channel
            } for output in Video.objects.all()
        ]
        return Response(output)
    def post(self,request):
        serializer = VideoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
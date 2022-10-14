import os

from rest_framework import generics
from rest_framework.views import APIView, Request, Response, status

from .models import File
from .serializers import FileSerializer, FileUploaderSerializer

class ArchiveView(APIView):
    def post(self, request: Request)-> Response:
        

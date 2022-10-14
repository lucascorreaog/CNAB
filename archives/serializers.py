from dataclasses import fields
from .models import File, FileUploader
from rest_framework import serializers


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"


class FileUploaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUploader
        fields = "__all__"

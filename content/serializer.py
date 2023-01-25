from rest_framework import serializers
from .models import FileModel, ContentModel

class FileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileModel
        fields = "__all__"

class ContentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentModel
        fields = "__all__"
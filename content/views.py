from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import FileModel, ContentModel
from users.models import ProfileModel
from setups.models import ProductType
from .serializer import FileModelSerializer, ContentModelSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from django.http import HttpResponse, JsonResponse

# Create your views here.
class FileModelView( viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = FileModelSerializer
    queryset = FileModel.objects.all()

# Create your views here.
class ContentModelView( viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ContentModelSerializer
    queryset = ContentModel.objects.all()
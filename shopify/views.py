from django.shortcuts import render
from .models import UserVerifyModel
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import UserVerifyModelSerializer
from django.http import JsonResponse
import json

# Create your views here.
class UserVerifyView( viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserVerifyModelSerializer
    queryset = UserVerifyModel.objects.all()

    @action(detail=False, methods=['POST'], url_path='test')
    def re_order(self, request):
        json_data = json.loads(request.body)
        print ( json_data)
        return JsonResponse({"Works": "testsssssssssssssssssssssssssss"})
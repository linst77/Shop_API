from django.shortcuts import render
from .models import UserVerifyModel, OrderModel
from .serializer import UserVerifyModelSerializer,OrderModelSerializer

from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class UserVerifyView( viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserVerifyModelSerializer
    queryset = UserVerifyModel.objects.all()

class OrderView( viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = OrderModelSerializer
    queryset = OrderModel.objects.all()




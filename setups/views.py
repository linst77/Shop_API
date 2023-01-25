from django.shortcuts import render

# Create your views here.
from .models import ProductType
from users.models import UserVerifyModel
from .serializer import ProductTypeSerializer
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response


class ProductTypeView( viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ProductTypeSerializer
    queryset = ProductType.objects.all()



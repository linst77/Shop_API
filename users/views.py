from django.shortcuts import render
from .models import UserVerifyModel, OrderModel
from .serializer import UserVerifyModelSerializer,OrderModelSerializer

from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import JsonResponse


# Create your views here.
class UserVerifyView( viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = UserVerifyModelSerializer
    queryset = UserVerifyModel.objects.all()


    @action(detail=False, methods=['POST'], url_path='create')
    def user_info( self, request):
        user_data = {
            "email" : request.data.get('email'),
            "phone": request.data.get('phone'),
            "first_name" : request.data.get('first_name'),
            "last_name": request.data.get('last_name'),
            "addresses" : str( request.data.get('addresses')),
            "shopify_id": request.data.get('id'),
            "currency" : request.data.get('currency')
        }
        serializer = self.serializer_class(data=user_data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.data, status=400)


class OrderView( viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = OrderModelSerializer
    queryset = OrderModel.objects.all()








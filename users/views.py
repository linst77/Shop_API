from django.shortcuts import render
from .models import UserVerifyModel, ProfileModel, OrderModel
from setups.models import ProductType
from .serializer import UserVerifyModelSerializer, ProfileModelSerializer, OrderModelSerializer
from django.http import HttpResponse
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

    @action(detail=False, methods=['POST'], url_path='create')
    def make_order( self, request):
        customer_data = request.data.get("customer")
        customer = UserVerifyModel.objects.get(email=customer_data.get("email"))

        items = request.data.get("line_items")
        user_data = {
                        "product_title": None,
                        "product": None,
                        "order_number": request.data.get("order_number"),
                        "status": 1,
                        "email": customer.id,
                        "phone": customer_data.get("phone"),
                        "first_name": customer_data.get("first_name"),
                        "last_name": customer_data.get("last_name"),
                        "date": request.data.get("created_at"),
                     }
        values = []

        for i in items:
            for j in range( i.get("quantity")):
                try:
                    product_item = ProductType.objects.get(product_id=i.get("product_id"))
                    user_data["product_title"] = product_item.product_title
                    user_data["product"] = product_item.id

                    serializer = self.serializer_class(data=user_data)
                    if serializer.is_valid():
                        serializer.save()
                        values.append(serializer.data)
                except:
                    pass

        if len(values) > 1:
            return Response(values, status=201)
        elif len(values) == 1:
            return Response(values[0], status=201)
        else:
            return HttpResponse(status=404)


class ProfileView( viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ProfileModelSerializer
    queryset = ProfileModel.objects.all()

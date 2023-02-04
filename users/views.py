from django.shortcuts import render
from .models import UserVerifyModel, ProfileModel, OrderModel
from setups.models import ProductType
from content.models import FileModel
from content.serializer import FileModelSerializer
from .serializer import UserVerifyModelSerializer, ProfileModelSerializer, OrderModelSerializer
from setups.serializer import ProductTypeSerializer
from django.http import HttpResponse
from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

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

    @action(detail=True, methods=['GET'], url_path='userinfo')
    def make_order( self, request, pk):
        user_infor = []
        user_profile = self.queryset.get(order_id = pk)
        user_data = self.serializer_class(user_profile, many=False)

        orders = OrderModel.objects.get( id=pk)
        current_order = OrderModelSerializer( orders, many=False)

        product = ProductType.objects.get( id= current_order.data.get( "product"))
        current_product = ProductTypeSerializer( product, many=False)

        user_infor.append( user_data.data)
        user_infor.append( current_order.data)
        user_infor.append( current_product.data)

        return JsonResponse(user_infor, safe=False)
    '''
    @action(detail=True, methods=['PATCH'], url_path='edit')
    def patch_profile( self, request, pk):

        user_queryset = ProfileModel.objects.get( id = pk)
        serializer = ProfileModelSerializer( user_queryset, data=request.data, partial=True)
        print(serializer.__dict__)

        if serializer.is_valid():
            serializer.save()
            print ("working")
            print(serializer.data)
            return JsonResponse(data=serializer.data, many=False)
        else:
            print ("not working")
            return HttpResponse(status=500)
    '''

class ShopifyView( generics.GenericAPIView):
    permission_classes = [AllowAny]
    queryset = UserVerifyModel.objects.all()
    serializer_class = UserVerifyModelSerializer

    def get(self, request):
        return HttpResponse(status=201)

    def post(self, request):
        email = request.data.get("email")
        query_user = self.queryset.get(email = email)
        user = UserVerifyModelSerializer( query_user)
        return JsonResponse(user.data)

    def put(self, request):

        email_id = request.data.get("id")
        user_orders = OrderModel.objects.filter( email=email_id).order_by('-created')
        user_serializer = OrderModelSerializer( user_orders, many=True)

        if len(user_serializer.data) == 0:
            return HttpResponse( status=404)

        return JsonResponse(user_serializer.data, safe=False)

class ShopifyUserProfile( APIView):

    def put(self, request, pk, *args, **kwargs):
        profile_object = ProfileModel.objects.get(id=pk)
        serializer = ProfileModelSerializer( profile_object, data =request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data)

        return HttpResponse(status=404)

class ShopifyUserFiles( APIView):

    def get(self, request, pk, pk2):
        user_order = OrderModel.objects.get( id=pk)
        user_product = ProductType.objects.get( id=pk2)

        if user_product.id == user_order.product_id:
            items = user_product.items
            all_file = FileModel.objects.filter( order_id = pk)
            return_value = []

            for i in range( items):
                temp = all_file.filter( items = i).order_by('orders')
                serializer = FileModelSerializer( temp, many=True)
                return_value.append( serializer.data)

            return Response (tuple(return_value))
        return HttpResponse( status=404)



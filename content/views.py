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

    @action(detail=False, methods=['PATCH'], url_path='fileorder')
    def re_order(self, request):
        update = []
        for i in request.data:
            temp = self.queryset.get(id=i["id"])
            temp.orders = i.get('orders')
            update.append(temp)

        FileModel.objects.bulk_update(update, ['orders'])
        return JsonResponse({"Works": "test"})


# Create your views here.
class ContentModelView( viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = ContentModelSerializer
    queryset = ContentModel.objects.all()

    @action(detail=True, methods=['GET'], url_path='context')
    def make_order(self, request, pk):

        object = self.queryset.get(id = pk)
        serializer = self.serializer_class( object, many=False)

        return JsonResponse(serializer.data)
        # return JsonResponse(user_infor, safe=False)

    @action(detail=True, methods=['PATCH'], url_path='cur-content')
    def patch_content( self, request, pk=None):
        temp = ContentModel.objects.get(id=pk)
        temp.sub_title = request.data.get("sub_title")
        patch_update = [temp]
        ContentModel.objects.bulk_update( patch_update, ['sub_title'])
        serialize = self.serializer_class( temp, many=False)
        return JsonResponse(serialize.data)

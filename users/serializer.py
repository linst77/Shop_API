from rest_framework import serializers
from .models import UserVerifyModel, OrderModel

class UserVerifyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVerifyModel
        fields = "__all__"

class OrderModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = "__all__"

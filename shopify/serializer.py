from rest_framework import serializers
from .models import UserVerifyModel

class UserVerifyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserVerifyModel
        fields = "__all__"
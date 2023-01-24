from django.contrib import admin
from .models import UserVerifyModel, OrderModel

@admin.register( UserVerifyModel)
class UserAdmin( admin.ModelAdmin):
    list_display = ['id']

@admin.register( OrderModel)
class OrderAdmin( admin.ModelAdmin):
    list_display = ['id']


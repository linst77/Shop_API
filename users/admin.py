from django.contrib import admin
from .models import UserVerifyModel, OrderModel

@admin.register( UserVerifyModel)
class UserAdmin( admin.ModelAdmin):
    list_display = ['id', 'email', 'currency']

@admin.register( OrderModel)
class OrderAdmin( admin.ModelAdmin):
    list_display = ['id',  'order_number', 'email', 'product_id']


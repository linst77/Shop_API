from django.contrib import admin
from .models import UserVerifyModel, OrderModel, ProfileModel

@admin.register( UserVerifyModel)
class UserAdmin( admin.ModelAdmin):
    list_display = ['id', 'email', 'currency']

@admin.register( OrderModel)
class OrderAdmin( admin.ModelAdmin):
    list_display = ['id',  'order_number', 'status', 'email', 'product', 'date']

@admin.register( ProfileModel)
class ProfileAdmin( admin.ModelAdmin):
    list_display = ['id', 'order', 'email', 'product']

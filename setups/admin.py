from django.contrib import admin
from .models import ProductType

@admin.register( ProductType)
class ProductAdmin( admin.ModelAdmin):
    list_display = ['id', 'product_title', 'product_id']
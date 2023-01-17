from django.contrib import admin
from .models import UserVerifyModel

# Register your models here.
@admin.register( UserVerifyModel)
class FileAdmin( admin.ModelAdmin):
    list_display = ['id', 'user_mail', 'user_phone']

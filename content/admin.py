from django.contrib import admin
from .models import ContentModel, FileModel

# Register your models here.
@admin.register( ContentModel)
class ProductAdmin( admin.ModelAdmin):
    list_display = ['id', 'order', 'email', 'product']
    raw_id_fields = (
        "photo_0",
        "photo_1",
        "photo_2",
        "photo_3",
        "photo_4",
        "photo_5",
        "photo_6",
        "photo_7",
        "photo_8",
        "photo_9",
        "photo_10",
        "photo_11",
        "photo_12",
        "photo_13",
        "photo_14",
         )

@admin.register( FileModel)
class FileModel( admin.ModelAdmin):
    list_display = ['id', 'order', 'email', 'product','items', 'counts']
from django.db import models
from users.models import UserVerifyModel, OrderModel, ProfileModel
from setups.models import ProductType
import os
from .image_detact import de_alpha, de_thumb
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

# Create your models here.
def file_path(instance, filename):
    return os.path.join(f'images/{instance.email_id}/{instance.order_id}/{filename}')

def thumb_file_path(instance, filename):
    return os.path.join(f'images/{instance.email_id}/{instance.order_id}/thumb/thum_{filename}')

# Create your models here.
class FileModel( models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    email = models.ForeignKey( UserVerifyModel, on_delete=models.CASCADE, related_name='file_user', blank=True, null=True)
    product = models.ForeignKey( ProductType, on_delete=models.PROTECT, related_name='file_product_type', blank=True, null=True)
    profile = models.ForeignKey( ProfileModel, on_delete=models.CASCADE, blank=True, null=True, related_name="file_profile")
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, blank=True, null=True, related_name="file_order")

    files = models.FileField( upload_to=file_path, null=True, blank=True)
    thumbnail = models.ImageField( upload_to=thumb_file_path, null=True, blank=True)
    items = models.IntegerField(null=True, blank=True)
    orders = models.IntegerField(null=True, blank=True)
    counts = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str( self.product)

    def save(self, *args, **kwargs):
        size_wh = (200, 112)
        # Original Image
        if not self.files:
            return None
        else:
            self.files = de_alpha( self.files)
            self.thumbnail = de_thumb( self.files)
        super(FileModel, self).save(*args, **kwargs)

class ContentModel( models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    email = models.ForeignKey( UserVerifyModel, on_delete=models.CASCADE, related_name='content_user', blank=True, null=True)
    product = models.ForeignKey( ProductType, on_delete=models.PROTECT, related_name='content_product', blank=True, null=True)
    profile = models.ForeignKey( ProfileModel, on_delete=models.CASCADE, blank=True, null=True, related_name="content_profile")
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, blank=True, null=True, related_name="content_order")

    photo_0 = models.ManyToManyField( FileModel, related_name="item_01", blank=True)
    photo_1 = models.ManyToManyField( FileModel, related_name="item_02",  blank=True)
    photo_2 = models.ManyToManyField( FileModel, related_name="item_03",  blank=True)
    photo_3 = models.ManyToManyField( FileModel, related_name="item_04",  blank=True)
    photo_4 = models.ManyToManyField( FileModel, related_name="item_05",  blank=True)
    photo_5 = models.ManyToManyField( FileModel, related_name="item_06",   blank=True)
    photo_6 = models.ManyToManyField( FileModel, related_name="item_07",   blank=True)
    photo_7 = models.ManyToManyField( FileModel, related_name="item_08",  blank=True)
    photo_8 = models.ManyToManyField( FileModel, related_name="item_09",  blank=True)
    photo_9 = models.ManyToManyField( FileModel, related_name="item_10",   blank=True)
    photo_10 = models.ManyToManyField( FileModel, related_name="item_11",   blank=True)
    photo_11 = models.ManyToManyField( FileModel, related_name="item_12",   blank=True)
    photo_12 = models.ManyToManyField( FileModel, related_name="item_13",  blank=True)
    photo_13 = models.ManyToManyField( FileModel, related_name="item_14",   blank=True)
    photo_14 = models.ManyToManyField( FileModel, related_name="item_15",  blank=True)
    sub_title = models.TextField( blank=True, null=True)
    option = models.TextField( blank=True, null=True)

    def __str__(self):
        return str( self.email)

    @receiver(post_save, sender=ProfileModel)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:

            try:
                product = ProductType.objects.get( pk = instance.product_id)
                email = UserVerifyModel.objects.get( pk = instance.email_id)
                order = OrderModel.objects.get( pk = instance.order_id)
                profile = ProfileModel.objects.get( pk=instance.id)
            except:
                product = None
                email = None
                order = None
                profile = None

            ContentModel.objects.create(
                                        email=email,
                                        product = product,
                                        order = order,
                                        profile = profile
                                    )

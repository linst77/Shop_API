from django.db import models
from django.utils.text import slugify
import string, random
from setups.models import ProductType
from django.db.models.signals import post_save
from django.dispatch import receiver
import json


# Create your models here.
class UserVerifyModel(models.Model):
    ### This is login ###
    id = models.AutoField(primary_key=True, editable=False)
    email = models.EmailField(max_length=254, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    addresses = models.TextField(blank=True, null=True)
    shopify_id = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.id) + ":" + str(self.email)

# order status

STATUS_CHOICES = (
    (1, 'Waiting to start'),
    (2, 'Processing'),
    (3, 'Review'),
    (4, 'Deliveried'),
    (5, 'Retake'),
    (6, 'Canceled'),
)

class OrderModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    product_title = models.CharField(max_length=200, blank=True, null=True)
    product = models.ForeignKey( ProductType, on_delete=models.CASCADE, related_name="product_num", blank=True, null=True)
    order_number = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField( choices=STATUS_CHOICES, default=1)

    email = models.ForeignKey(UserVerifyModel, on_delete=models.CASCADE, related_name="OrderModel", blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ":" + str(self.order_number)




class ProfileModel( models.Model):

    id = models.AutoField(primary_key=True, editable=False)

    ### Login info ###
    email = models.ForeignKey( UserVerifyModel, on_delete=models.CASCADE, related_name="ProfileModel", blank=True, null=True)
    phone = models.CharField( max_length=200, blank=True, null=True)

    ### User Information
    first_name = models.CharField( max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    name_a = models.CharField( max_length=200, blank=True, null=True)
    name_b = models.CharField( max_length=200, blank=True, null=True)
    name_c = models.CharField( max_length=200, blank=True, null=True)
    name_d = models.CharField( max_length=200, blank=True, null=True)

    location = models.CharField( max_length=200, blank=True, null=True)
    event_date = models.CharField( max_length=200, blank=True, null=True)

    ### product type
    order = models.ForeignKey( OrderModel,  on_delete=models.CASCADE, blank=True, null=True, related_name="ProfileModel_order")
    product = models.ForeignKey( ProductType, on_delete=models.CASCADE, blank=True, null=True, related_name="ProfileModel_product")

    ### process steps
    preview = models.URLField(  max_length=200, blank=True, null=True)
    finalview = models.URLField( max_length=200, blank=True, null=True)

    ## extra
    extra_info = models.TextField(blank=True, null=True)

    def __str__( self):
        return str( self.id) + ":" + str(self.email)

    #def save(self, *args, **kwargs):
    #    if self.product_type != None:
    #        self.pre_product_type = self.product_type
    #    super(ProfileModel, self).save(*args, **kwargs)

    @receiver(post_save, sender=OrderModel)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            try:
                product = ProductType.objects.get( pk = instance.product_id)
                email = UserVerifyModel.objects.get( pk = instance.email_id)
                order = OrderModel.objects.get( pk = instance.id)
            except:
                product = None
                email = None
                order = None

            ProfileModel.objects.create(
                                            email = email,
                                            product=product,
                                            first_name = instance.first_name,
                                            last_name=instance.last_name,
                                            phone = instance.phone,
                                            order = order
                                        )

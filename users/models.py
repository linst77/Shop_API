from django.db import models
from django.utils.text import slugify
import string, random


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
        return str(self.email)

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
    product_id = models.CharField(max_length=200, blank=True, null=True)
    order_number = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField( choices=STATUS_CHOICES, default=1)

    email = models.ForeignKey(UserVerifyModel, on_delete=models.CASCADE, related_name="user_mail_sel", blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)

    first_name = models.CharField(max_length=200, blank=True, null=True)
    last_name = models.CharField(max_length=200, blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.order_number)
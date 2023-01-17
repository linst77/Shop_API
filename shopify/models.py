from django.db import models

# Create your models here.

class UserVerifyModel( models.Model):
    ### This is login ###
    user_mail = models.EmailField( max_length=254, blank=True, null=True)
    user_phone = models.IntegerField( blank=True, null=True)

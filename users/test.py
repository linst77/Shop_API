from django.db import models
from django.utils.text import slugify
import string, random


# Create your models here.


class UserVerifyModel(models.Model):
    ### This is login ###
    id = models.AutoField(primary_key=True, editable=False)
    user_mail = models.EmailField(max_length=254, blank=True, null=True)
    user_phone = models.IntegerField(blank=True, null=True)

    ### Extra information ###
    order_name = models.CharField(max_length=200, blank=True, null=True)
    nation = models.IntegerField(blank=True, null=True)
    store = models.IntegerField(blank=True, null=True)
    product_category = models.IntegerField(blank=True, null=True)
    product_type = models.IntegerField(blank=True, null=True)
    process_step = models.IntegerField(default=0, blank=True, null=True)
    menu = models.IntegerField(default=0, blank=True, null=True)

    # product_type = models.ForeignKey( ProductType, on_delete=models.CASCADE, blank=True, null=True)
    option = models.CharField(max_length=100, blank=True, null=True)
    slug = models.SlugField(db_index=True, unique=True, max_length=200, blank=True, null=True)

    def __str__(self):
        return str(self.user_mail)

    def save(self, *args, **kwargs):
        slug_suffix = []
        for i in range(30):
            slug_suffix.append(random.choice(string.ascii_letters))
        slug = slugify(str(self.user_mail) + ''.join(slug_suffix), allow_unicode=True)
        self.slug = slug
        super(UserVerifyModel, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.user_mail)


class OrderModel(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    order_number = models.AutoField
    status =

    user_mail = models.ForeignKey(UserVerifyModel, on_delete=models.CASCADE, related_name="user_mail_sel")
    phone = customer.phone

    first_name = customer.first_name
    last_name = customer.last_name
    date = updated_at

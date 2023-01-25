from django.db import models


class ProductType( models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    product_title = models.CharField(max_length=200, blank=True, null=True)
    product_id = models.CharField( max_length=200, blank=True, null=True)

    items = models.IntegerField(blank=True, null=True)
    counts = models.CharField( max_length=200, blank=True, null=True)
    input_box = models.CharField( max_length=200, blank=True, null=True)
    description_index = models.CharField( max_length=300, blank=True, null=True)
    content_text = models.TextField(blank=True, null=True)
    front_content_text = models.CharField( max_length=200, blank=True, null=True)
    guide_text = models.CharField( max_length=200, blank=True, null=True)
    image_url = models.URLField(  max_length=200, blank=True, null=True)
    review_url = models.URLField(  max_length=200, blank=True, null=True)
    parts = models.CharField( max_length=500, null=True, blank=True)

    def __str__( self):
        return str( self.id) + ": " +  str( self.product_title)

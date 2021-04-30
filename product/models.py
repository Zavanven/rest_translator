from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    sku = models.CharField(max_length=50)
    id_product = models.IntegerField()
    category = models.CharField(max_length=200)
    shipping_class = models.IntegerField()
    image_url = models.URLField(blank=True)
    price_b2b = models.FloatField()
    price_b2c = models.FloatField()
    pa_color = models.CharField(max_length=50, blank=True)
    pa_type = models.CharField(max_length=50, blank=True)
    pa_year = models.CharField(max_length=50, blank=True)
    pa_wheels = models.CharField(max_length=50, blank=True)
    pa_model = models.CharField(max_length=100, blank=True)
    pa_class = models.CharField(max_length=100, blank=True)
    pa_brand = models.CharField(max_length=50, blank=True)
    pa_battery = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
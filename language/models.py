from django.db import models
from shop.models import Shop

# Create your models here.
class Language(models.Model):
    title = models.CharField(max_length=100)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
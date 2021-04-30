from django.db import models
from product.models import Product
from language.models import Language

class Translation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title
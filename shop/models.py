from django.db import models

# Create your models here.
class Shop(models.Model):
    title = models.CharField(max_length=100)
    consumer_key = models.CharField(max_length=60, blank=True)
    consumer_secret = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.title


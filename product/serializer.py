from django.db.models import fields
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'sku',
            'id_product',
            'category',
            'shipping_class',
            'image_url',
            'price_b2b',
            'price_b2c',
            'pa_color',
            'pa_type',
            'pa_year',
            'pa_wheels',
            'pa_model',
            'pa_class',
            'pa_brand',
            'pa_battery',
            'description',
            )
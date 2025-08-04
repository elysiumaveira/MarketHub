from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'description', 'price', 
                'sub_category', 'image', 'thumbnail', 'is_active']
        extra_kwargs = {
            'slug': {'required': False},
            'image': {'required': False},
            'thumbnail': {'required': False},
        }
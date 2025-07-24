from rest_framework import serializers
from .models import MainCategory, SubCategory


class MainCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = MainCategory
        fields = ['id', 'name', 'slug','is_active']
        extra_kwargs = {
            'slug': {'required': False}
        }


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'slug','is_active']
        extra_kwargs = {
            'slug': {'required': False}
        }

from rest_framework import serializers
from .models import User
from products.serializer import ProductSerializer


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'phone_number']


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserSerializer(serializers.ModelSerializer):
    favorite_products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'avatar', 'favorite_products']

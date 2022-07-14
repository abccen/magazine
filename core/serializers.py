from django.contrib.auth.models import User
from rest_framework import serializers

from core.models import Products, Category


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField

    class Meta:
        model = Products
        fields = ('id', 'name', 'price', 'description', 'image', 'category', 'user')

        extra_kwargs = {'user': {'read_only': True}}



    # def create(self, validated_data):
    #     product = Products(**validated_data)
    #     product.user = self.context.get('request').user
    #     product.save()
    #     return product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

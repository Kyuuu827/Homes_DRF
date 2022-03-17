from rest_framework import serializers
from .models        import *


class SubCategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class CategorySerializer(serializers.Serializer):
    name          = serializers.CharField(max_length=100)
    subcategories = SubCategorySerializer(many=True)

class MenuSerializer(serializers.Serializer):
    menu_name  = serializers.CharField(max_length=100)
    image_url  = serializers.CharField(max_length=100)
    categories = CategorySerializer(many=True)


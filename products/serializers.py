from rest_framework import serializers
from .models        import *

# class MenuSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Menu, Category, SubCategory
#         fields = '__all__'

# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

# class SubCategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = SubCategory
#         fields = '__all__'

class SubCategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)

class CategorySerializer(serializers.Serializer):
    name          = serializers.CharField(max_length=100)
    subcategories = SubCategorySerializer(many=True)

class MenuSerializer(serializers.Serializer):
    menu_name  = serializers.CharField(max_length=100)
    image_url  = serializers.CharField(max_length=100)
    categories = CategorySerializer(many=True)


from rest_framework.serializers import ModelSerializer
from rest_framework.fields      import CharField

from .models        import *


class SubCategorySerializer(ModelSerializer):
    name = CharField(max_length=100)

    class Meta:
        model = SubCategory
        fields = '__all__'

class CategorySerializer(SubCategorySerializer):
    name = CharField(max_length=100)
    subcategories = SubCategorySerializer(source='subcategory_set',many=True)

    class Meta: 
        model = Category
        fields = 'name', 'subcategories'

class MenuSerializer(CategorySerializer):
    name       = CharField(max_length=100)
    image_url  = CharField(max_length=100)
    categories = CategorySerializer(source='category_set', many=True)

    class Meta:
        model = Menu
        fields = 'name', 'image_url', 'categories'
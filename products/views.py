import json

from django.http.response    import JsonResponse
from django.views            import View
from django.db.models        import Avg, Count, F
from rest_framework          import viewsets, views
from rest_framework.response import Response
from rest_framework.decorators import action

from .models                 import Menu, Category, SubCategory, ProductGroup
from .serializers            import MenuSerializer


class MenuListViewSet(viewsets.ViewSet):
    def get(self, request):
        menus = Menu.objects.prefetch_related('category_set', 'category_set__subcategory_set').all()

        menu_data = [{
            'menu_id'   : menu.id,
            'menu_name' : menu.name,
            'image_url' : menu.image_url,
            'categories'  : [{
                'id'   : category.id,
                'name' : category.name,
                'subcategories'   : [{
                    'id'   : subcategory.id,
                    'name' : subcategory.name,
                } for subcategory in category.subcategory_set.all()],
            } for category in menu.category_set.all()],
        } for menu in menus]

        serializer = MenuSerializer(menu_data, many = True)
        
        return Response(serializer.data)
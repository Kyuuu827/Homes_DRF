from django.urls            import path, include
from rest_framework.routers import DefaultRouter

from products import views


# router = DefaultRouter(trailing_slash=False)
# router.register(r'menus', views.MenuListViewSet, basename = 'MenuList')

urlpatterns = [
    # path('', include(router.urls)),
	path('menus', views.MenuListViewSet.as_view(), name = 'menu-list'), 
]
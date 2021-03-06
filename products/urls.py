from django.urls            import path, include
from rest_framework.routers import DefaultRouter

from products import views


router = DefaultRouter(trailing_slash=False)
router.register(r'menus', views.MenuListViewSet, basename = 'MenuList')
router.register(r'', views.ProductGroupsViewSet, basename = 'ProductGroups')

urlpatterns = [
    path('', include(router.urls)),
    path('<int:id>', views.ProductGroupViewSet.as_view)
	#path('menus', views.MenuListViewSet.as_view({'get':'list'}), name = 'menu-list'), 
]
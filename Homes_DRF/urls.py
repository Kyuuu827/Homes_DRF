from django.contrib        import admin
from django.urls           import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    #path('users', include('users.urls')),

    #api docs
    path('schema', SpectacularAPIView.as_view(), name='schema'),
    path('swagger', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger'),
    path('redoc', SpectacularRedocView.as_view(url_name='schema'), name='redoc')
]
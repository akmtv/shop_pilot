from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import api_root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api_root'),
    path('api/products/', include('apps.products.urls')),
    path('api/categories/', include('apps.categories.urls')),
    path('api_auth/', include('rest_framework.urls')),
<<<<<<< HEAD
    path('api/users/', include('apps.users.urls'))
=======
    path('api/users/', include('apps.users.urls')),
    path('api/carts/', include('apps.carts.urls'))
>>>>>>> 37228d8634f9299cb08dc0a0af3415304659af19
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

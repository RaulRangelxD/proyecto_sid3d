from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name= 'index'),
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
    path('login/', include('login.urls')),
    
]

    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_productos'),
    path('ver/', views.ver, name='ver'),
    path('crear/', views.crear, name='crear'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('borrar/<str:nombre>', views.borrar, name='borrar'),
    path('editar/<str:nombre>', views.editar, name='editar'),
    path('busqueda/<categoria>', views.busqueda, name='busqueda'),
]
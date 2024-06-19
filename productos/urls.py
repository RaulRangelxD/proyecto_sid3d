from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('crear/', views.crear, name='crear'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('ver/<str:nombre>', views.ver, name='ver'),
    path('borrar/<str:nombre>', views.borrar, name='borrar'),
    path('editar/<str:nombre>', views.editar, name='editar'),
    path('busqueda/<categoria>', views.busqueda, name='busqueda'),
]
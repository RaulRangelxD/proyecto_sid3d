from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.productos, name='productos'),
    path('productos_eliminados/', views.productos_eliminados, name='productos_eliminados'),
    path('crear/', views.crear, name='crear'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
    path('ver/<str:nombre>', views.ver, name='ver'),
    path('borrar/<str:nombre>', views.borrar, name='borrar'),
    path('restaurar/<str:nombre>', views.restaurar, name='restaurar'),
    path('editar/<str:nombre>', views.editar, name='editar'),
    path('busqueda/<categoria>', views.busqueda, name='busqueda'),
    path('carrito/', views.carrito, name='carrito'),
    path('confirmar_compra/', views.confirmar_compra, name='confirmar_compra'),
    path('compras_confirmadas/', views.compras_confirmadas, name='compras_confirmadas'),

    path('logout/', views.logout_view, name='logout'),
]
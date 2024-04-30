from django.urls import path
from .views import index, ver, crear, borrar, editar

urlpatterns = [
    path('', index),
    path('ver/', ver),
    path('crear/', crear),
    path('borrar/<str:nombre>', borrar),
    path('editar/<str:nombre>', editar),
]
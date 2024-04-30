from django.urls import path
from .views import user_login, registrar_usuario

urlpatterns = [
    path('iniciar_sesion/', user_login, name='login'),
    path('registrar/', registrar_usuario),
]
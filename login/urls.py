from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name= 'index'),
    path('loggearse/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/',  views.edit_user_view, name='user_edit'),
    path('edit_password',  views.edit_password, name='edit_password'),
    path('profile/',  views.profile, name='profile'),
    
]


from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name= 'index'),
    path('loggearse/', views.login_view, name='login_view'),
    path('register/', views.register, name='register'),
    path('adminpage/', views.admin, name='adminpage'),
    path('customer/', views.customer, name='customer'),
    path('employee/', views.employee, name='employee'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('edit/',  views.edit_user_view, name='user_edit'),
    
]


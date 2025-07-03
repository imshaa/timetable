from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
   path('', views.register, name='register'),
   path('register/', views.register, name='register'),
   path('loginpage/', views.loginpage, name='loginpage'),
   path('index/', views.index, name='index'),
   path('logoutpage/', views.logoutpage, name='logoutpage')
]

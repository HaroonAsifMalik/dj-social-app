from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('home/', views.home, name='home'),
    path('logout/', views.user_logout, name='user_logout'),
]

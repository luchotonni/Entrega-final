from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('perfil/', views.perfil, name='perfil'),
    path('crear_producto/', views.crear_producto, name='crear_producto'),
    path('crear_categoria/', views.crear_categoria, name='crear_categoria'),
]

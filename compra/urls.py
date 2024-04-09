from django.urls import path
from . import views

urlpatterns = [
    path('crearProveedor/', views.nuevo_proveedor),
    path('crearProducto/', views.nuevo_producto), 
]
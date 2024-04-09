from django.urls import path
from . import views

urlpatterns = [
    path('crearProveedor/', views.nuevo_proveedor),
    path('crearProducto/', views.nuevo_producto), 
    path('listaProductos', views.mostrar_productos),
    path('listaProveedores', views.mostrar_proveedores),
    path('actualizarProducto/<str:nombre>', views.update_producto_nombre),
    path('actualizarProveedor/<int:dni>', views.update_proveedor_dni),
    path('filtrarProducto/<int:precio>', views.filtrar_productos_precio),
    path('filtrarProveedor/<int:dni>', views.filtrar_proveedor_dni),
    path('borrarProducto/<str:nombre>', views.delete_producto_nombre), 
    path('borrarProductos', views.delete_all),
    path('borrarProveedor/<int:dni>', views.delete_proveedor_dni), 
    path('borrarProveedores', views.delete_all),
]
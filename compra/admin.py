from django.contrib import admin
from .models import Proveedor, Producto

# Register your models here.
class ProveedorAdmin(admin.ModelAdmin):
    list_display=["nombre", "apellido", "dni"]
    search_fields=["nombre", "apellido", "dni"]

class ProductoAdmin(admin.ModelAdmin):
    list_display=["nombre", "precio", "stock_actual"]
    search_fields=["nombre", "precio", "stock_actual"]

admin.site.register(Proveedor,ProveedorAdmin),
admin.site.register(Producto,ProductoAdmin)

#USER: FATIMAALFARO
#PASSWORD:2586
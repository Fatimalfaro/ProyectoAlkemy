from django.shortcuts import render
from .formsproveedor import ProveedorForm
from django.http import HttpResponse
from .formsproducto import ProductoForm
from .models import Producto, Proveedor
from django.template import Template, Context

def nuevo_proveedor(request):
    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ProveedorForm()
    return render(request, 'crear_proveedor.html', {'form': form})

def nuevo_producto(request):
    proveedores = Proveedor.objects.all()
    context = {
        'proveedores':proveedores
    }
    if request.POST:
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        stock_actual = request.POST['stock_actual'] 
        proveedor_id = request.POST['proveedor']

        Producto.objects.create(
            nombre = nombre,
            precio=precio,
            stock_actual=stock_actual,
            proveedor_id=proveedor_id,
        )
    return render(request, 'crear_producto.html', context)

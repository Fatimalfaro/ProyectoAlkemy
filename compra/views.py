from django.shortcuts import render
from .formsproveedor import ProveedorForm
from django.http import HttpResponse
from .formsproducto import ProductoForm
from .models import Producto, Proveedor
from django.template import Template, Context


#Realizo el CRUD de proveedor y producto 
#Crear
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

#Leer/Mostrar
#Mostrar todos los productos
def mostrar_productos(request):
    productos = Producto.objects.all()
    ruta = "C:/Users/fatia/OneDrive/Escritorio/Proyecto - Alkemy/StockControl/compra/templates/listar_productos.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({'productos': productos})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

#Mostrar todos los proveedores/Bonus
def mostrar_proveedores(request):
    proveedores = Proveedor.objects.all()
    ruta = "C:/Users/fatia/OneDrive/Escritorio/Proyecto - Alkemy/StockControl/compra/templates/listar_proveedores.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({'proveedores': proveedores})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

#Actualizar
#Actualizar proveedor por su dni
def update_proveedor_dni(request, dni):
    proveedorActualizar = Proveedor.objects.get(dni = dni)
    proveedorActualizar.nombre = "Pamela"
    proveedorActualizar.apellido = "Sanchez"
    proveedorActualizar.dni = 1254789
    proveedorActualizar.save()
    ruta = "C:/Users/fatia/OneDrive/Escritorio/Proyecto - Alkemy/StockControl/compra/templates/proveedores_actualizados.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({'proveedorActualizar': proveedorActualizar})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

#Actualizar producto por su nombre
def update_producto_nombre(request, nombre):
    productoActualizar = Producto.objects.get(nombre = nombre)
    productoActualizar.nombre = "Heladera"
    productoActualizar.precio = 800000
    productoActualizar.stock_actual = 5
    productoActualizar.save()
    ruta = "C:/Users/fatia/OneDrive/Escritorio/Proyecto - Alkemy/StockControl/compra/templates/productos_actualizados.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({'productoActualizar':  productoActualizar})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

#Filtrar
#Mostrar productos filtrados por precio
def filtrar_productos_precio(request, precio):
    productoEncontrado = Producto.objects.filter(precio=precio)
    ruta = "C:/Users/fatia/OneDrive/Escritorio/Proyecto - Alkemy/StockControl/compra/templates/productos_filtrados.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({'productoEncontrado': productoEncontrado})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

#Mostrar proveedores filtrados por dni - R
def filtrar_proveedor_dni(request, dni):
    proveedorEncontrado = Proveedor.objects.filter(dni=dni)
    ruta = "C:/Users/fatia/OneDrive/Escritorio/Proyecto - Alkemy/StockControl/compra/templates/proveedores_filtrados.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({'proveedorEncontrado': proveedorEncontrado})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

#Borrar
#Borrar todos los proveedores 
def delete_all(request):
    proveedores = Proveedor.objects.all()
    proveedores.delete()
    ruta = "C:/Users/fatia/OneDrive/Escritorio/Proyecto - Alkemy/StockControl/compra/templates/listar_proveedores.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({'proveedores':  proveedores})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

#Borrar proveedores por su dni 
def delete_proveedor_dni(request, dni):
    proveedorBorrar = Proveedor.objects.get(dni = dni)
    proveedorBorrar.delete()
    proveedores = Proveedor.objects.all()
    ruta = "C:/Users/fatia/OneDrive/Escritorio/Proyecto - Alkemy/StockControl/compra/templates/listar_proveedores.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({'proveedores':  proveedores})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

#Borrar todos los productos 
def delete_all(request):
    productos = Producto.objects.all()
    productos.delete()
    ruta = "C:/Users/fatia/OneDrive/Escritorio/Proyecto - Alkemy/StockControl/compra/templates/listar_productos.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({'productos' : productos})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)

#Borrar producto por su nombre
def delete_producto_nombre(request, nombre):
    productoBorrar = Producto.objects.get(nombre = nombre)
    productoBorrar.delete()
    productos = Producto.objects.all()
    ruta = "C:/Users/fatia/OneDrive/Escritorio/Proyecto - Alkemy/StockControl/compra/templates/listar_productos.html"
    doc_externo = open(ruta)
    plantilla = Template(doc_externo.read())
    doc_externo.close()
    contexto = Context({'productos':  productos})
    documento = plantilla.render(contexto)
    return HttpResponse(documento)


from django.shortcuts import render, redirect
from .models import OrdenTrabajo
from .models import Mecanico
from .models import Tarea
from .forms import OrdenTrabajoForm

# Create your views here.

# Vista para listar todas las órdenes de trabajo
def lista_ordenes(request):
    # Consultar todas las órdenes en la base de datos
    ordenes = OrdenTrabajo.objects.all()
    # Pasar las órdenes al template como contexto
    return render(request, 'lista_ordenes.html', {'ordenes': ordenes})

# Vista para listar todos los mecánicos
def lista_mecanicos(request):
    # Obtener todos los mecánicos desde la base de datos
    mecanicos = Mecanico.objects.all()
    # Renderizar la plantilla y pasar los mecánicos como contexto
    return render(request, 'lista_mecanicos.html', {'mecanicos': mecanicos})

# Vista para mostrar el detalle de una orden específica
def detalle_orden(request, orden_id):
    # Obtener la orden específica según su ID
    orden = OrdenTrabajo.objects.get(id=orden_id)
    # Renderizar la plantilla y pasar la orden como contexto
    return render(request, 'detalle_orden.html', {'orden': orden})


# Vista para listar todas las tareas
def lista_tareas(request):
    # Obtener todas las tareas desde la base de datos
    tareas = Tarea.objects.all()
    # Renderizar la plantilla y pasar las tareas como contexto
    return render(request, 'lista_tareas.html', {'tareas': tareas})


# Vista para crear una nueva orden de trabajo
def crear_orden(request):
    if request.method == 'POST':
        form = OrdenTrabajoForm(request.POST)
        if form.is_valid():
            form.save()  # Guardar la nueva orden en la base de datos
            return redirect('lista_ordenes')  # Redirigir a la lista de órdenes
    else:
        form = OrdenTrabajoForm()
    return render(request, 'crear_orden.html', {'form': form})


# Vista para buscar órdenes de trabajo
def buscar_orden(request):
    resultados = None
    if request.method == 'GET':
        form = BuscarOrdenForm(request.GET)
        if form.is_valid():
            cliente = form.cleaned_data.get('cliente')
            estado = form.cleaned_data.get('estado')
            resultados = OrdenTrabajo.objects.all()
            if cliente:
                resultados = resultados.filter(cliente__icontains=cliente)  # Filtro por cliente
            if estado:
                resultados = resultados.filter(estado=estado)  # Filtro por estado
    else:
        form = BuscarOrdenForm()
    return render(request, 'buscar_orden.html', {'form': form, 'resultados': resultados})





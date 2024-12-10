from django.shortcuts import render
from .models import OrdenTrabajo

# Create your views here.

# Vista para listar todas las órdenes de trabajo
def lista_ordenes(request):
    # Consultar todas las órdenes en la base de datos
    ordenes = OrdenTrabajo.objects.all()
    # Pasar las órdenes al template como contexto
    return render(request, 'lista_ordenes.html', {'ordenes': ordenes})



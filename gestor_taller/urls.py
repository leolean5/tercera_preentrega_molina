from django.urls import path
from . import views

urlpatterns = [
    path('ordenes/', views.lista_ordenes, name='lista_ordenes'),  # Lista de órdenes
    path('ordenes/crear/', views.crear_orden, name='crear_orden'),  # Crear una orden
    path('ordenes/<int:orden_id>/', views.detalle_orden, name='detalle_orden'),  # Detalle de una orden
    path('mecanicos/', views.lista_mecanicos, name='lista_mecanicos'),  # Lista de mecánicos
    path('tareas/', views.lista_tareas, name='lista_tareas'),  # Lista de tareas
    path('ordenes/buscar/', views.buscar_orden, name='buscar_orden'),  # Nueva ruta para buscar órdenes
]

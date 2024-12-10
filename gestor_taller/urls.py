from django.urls import path
from . import views

urlpatterns = [
    # Ruta para listar las órdenes de trabajo
    path('ordenes/', views.lista_ordenes, name='lista_ordenes'),
]

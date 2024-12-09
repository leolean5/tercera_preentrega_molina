from django.contrib import admin
from .models import Mecanico, OrdenTrabajo, Tarea

# Register your models here.

# Registrar los modelos en el panel de administración
admin.site.register(Mecanico)
admin.site.register(OrdenTrabajo)
admin.site.register(Tarea)

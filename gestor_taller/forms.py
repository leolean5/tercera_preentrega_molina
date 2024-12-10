from django import forms
from .models import OrdenTrabajo

# Formulario para Ordenes de Trabajo
class OrdenTrabajoForm(forms.ModelForm):
    class Meta:
        model = OrdenTrabajo
        fields = ['cliente', 'descripcion', 'mecanicos_asignados']  # Campos que se mostrarán en el formulario
        widgets = {
            'mecanicos_asignados': forms.CheckboxSelectMultiple()  # Para seleccionar múltiples mecánicos
        }

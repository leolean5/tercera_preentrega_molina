from django import forms
from .models import OrdenTrabajo

# Formulario para Ordenes de Trabajo
class OrdenTrabajoForm(forms.ModelForm):
    class Meta:
        model = OrdenTrabajo
        fields = ['cliente', 'descripcion', 'estado', 'mecanicos_asignados']  # Campos que se mostrarán en el formulario
        widgets = {
            'mecanicos_asignados': forms.CheckboxSelectMultiple()  # Para seleccionar múltiples mecánicos
        }

# Formulario para la busqueda de Ordenes      
class BuscarOrdenForm(forms.Form):
    cliente = forms.CharField(max_length=100, required=False)  # Campo para buscar por cliente
    estado = forms.ChoiceField(
        choices=[
            ('pendiente', 'Pendiente'),
            ('en_progreso', 'En Progreso'),
            ('completado', 'Completado'),
        ],
        required=False
    )

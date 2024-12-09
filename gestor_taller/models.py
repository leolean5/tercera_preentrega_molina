from django.db import models

# Create your models here.

# Clase para representar a los mecánicos
class Mecanico(models.Model):
    # Nombre del mecánico
    nombre = models.CharField(max_length=100)
    # Apellido del mecánico
    apellido = models.CharField(max_length=100)
    # Fecha de nacimiento del mecánico
    fecha_nacimiento = models.DateField()
    # Documento único del mecánico
    documento = models.CharField(max_length=20, unique=True)

    # Método para representar el objeto como cadena
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# Clase para representar una orden de trabajo
class OrdenTrabajo(models.Model):
    # Cliente asociado a la orden
    cliente = models.CharField(max_length=100)
    # Fecha de creación de la orden (automáticamente asignada al momento de crearla)
    fecha = models.DateTimeField(auto_now_add=True)
    # Descripción general de la orden de trabajo
    descripcion = models.TextField()
    # Estado de la orden con opciones predefinidas
    estado = models.CharField(
        max_length=20,
        choices=[
            ('pendiente', 'Pendiente'),
            ('en_progreso', 'En Progreso'),
            ('completado', 'Completado'),
        ],
        default='pendiente'  # Estado predeterminado al crear una nueva orden
    )
    # Relación muchos a muchos con la clase Mecanico
    # Una orden puede tener múltiples mecánicos asignados, y un mecánico puede estar en varias órdenes
    mecanicos_asignados = models.ManyToManyField(
        Mecanico,
        related_name="ordenes_trabajo"  # Nombre para acceder a las órdenes desde un mecánico
    )

    # Representación en formato cadena
    def __str__(self):
        return f"Orden {self.id} - {self.cliente}"


# Clase para representar tareas específicas dentro de una orden de trabajo
class Tarea(models.Model):
    # Tipo de tarea a realizar
    tipo_tarea = models.CharField(max_length=100)
    # Observaciones adicionales sobre la tarea
    observaciones = models.TextField(blank=True, null=True)
    # Relación con el mecánico que realizó la tarea
    mecanico = models.ForeignKey(
        Mecanico,
        on_delete=models.CASCADE,  # Si se elimina el mecánico, también se eliminarán sus tareas
        related_name="tareas"  # Nombre para acceder a las tareas desde un mecánico
    )
    # Fecha y hora en que se realiza la tarea
    fecha_hora = models.DateTimeField()
    # Relación con la orden de trabajo a la que pertenece la tarea
    orden_trabajo = models.ForeignKey(
        OrdenTrabajo,
        on_delete=models.CASCADE,  # Si se elimina la orden, también se eliminan sus tareas
        related_name="tareas"  # Nombre para acceder a las tareas desde una orden
    )

    # Representación en formato cadena
    def __str__(self):
        return f"Tarea: {self.tipo_tarea} - Orden {self.orden_trabajo.id}"

# Generated by Django 5.1.4 on 2024-12-09 23:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
                ('documento', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrdenTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=100)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField()),
                ('estado', models.CharField(choices=[('pendiente', 'Pendiente'), ('en_progreso', 'En Progreso'), ('completado', 'Completado')], default='pendiente', max_length=20)),
                ('mecanicos_asignados', models.ManyToManyField(related_name='ordenes_trabajo', to='gestor_taller.mecanico')),
            ],
        ),
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_tarea', models.CharField(max_length=100)),
                ('observaciones', models.TextField(blank=True, null=True)),
                ('fecha_hora', models.DateTimeField()),
                ('mecanico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='gestor_taller.mecanico')),
                ('orden_trabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tareas', to='gestor_taller.ordentrabajo')),
            ],
        ),
    ]
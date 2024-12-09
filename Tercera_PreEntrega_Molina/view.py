from django.http import HttpResponse
from django.template import Template, Context, loader
from datetime import datetime


def saludo(request):
    return HttpResponse("Hola, soy una primera view")

def segundo_saludo(request):
    return HttpResponse("<h1>Hola, soy una segunda view</h1>")

def dia_de_hoy(request):
    dia = datetime.datetime.now()
    documento_de_texto = f'Hoy es: <br> {dia}'
    return HttpResponse(documento_de_texto)

def mi_nombre(request, nombre):
    return HttpResponse(f"Mi nombre es: {nombre}")

def probandoTemplate(self):
    nombre = "Leandro"
    apellido = "Molina"
    notas = [10, 2, 4, 7, 3]
    
    diccionario = {"nombre": nombre, "apellido": apellido, "dia": datetime.now().date(), "notas": notas}
    
    plantilla = loader.get_template("template1.html")
    
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
from django.http import HttpResponse
import datetime
from django.template import Template, Context


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
    miHtml = open("Tercera_PreEntrega_Molina\plantillas\template1.html")
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)
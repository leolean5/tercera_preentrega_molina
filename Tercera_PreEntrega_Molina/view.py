from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Hola, soy una primera view")
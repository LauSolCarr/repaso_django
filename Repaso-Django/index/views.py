from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template import loader

# Create your views here.

def index(request):
    return HttpResponse('<h1>Bienvenido a mi pagina de Django<h1> ')

def plantilla(request):

    template = loader.get_template('plantilla.html')

    datos = {
        'lista' : ['primero' , 'segundo','tercero'],
        'nombre' : 'juancho'

    }

    plantilla_generada = template.render(datos)
    
    return HttpResponse(plantilla_generada)
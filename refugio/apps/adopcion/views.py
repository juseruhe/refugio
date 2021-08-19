from django.shortcuts import render

from django.http import HttpResponse, response

# Create your views here.

def index_adopcion(request):
    return HttpResponse("Es la Página Principal de Adopción")
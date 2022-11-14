from django.shortcuts import render
from urllib import request

def portada(request):
    return render (request, "portada.html")


def contacto(request):
    return render (request, "contacto.html")


def sobreMi(request):
    return render (request, "sobreMi.html")


def proyectos(request):
    return render (request, "proyectos.html")


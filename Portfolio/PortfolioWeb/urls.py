from django.urls import path
from PortfolioWeb.views import *

urlpatterns = [
    path('', portada),
    path("contacto", contacto),
    path("sobreMi", sobreMi),
    path("proyectos", proyectos),
]
from django.shortcuts import render, HttpResponse


html_cabecera = """ 
    <h1>Welcome</h1>
    <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/pelicula">pelicula</a></li>
    </ul>
"""


# Create your views here.
def home(request):
    return render(request,"core/home.html")

def presentacion(request):
    return render(request,"core/presentacion.html")

def contacto(request):
    return render(request,"core/contacto.html")


def pasatiempo(request):
    return render(request,"core/contacto.html")
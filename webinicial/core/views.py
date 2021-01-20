from django.shortcuts import render, HttpResponse

# Create your views here.
html_cabecera ="""
<h1>Welcome</h1>
<ul>
<li><a href="/">Home</li>
<li><a href="/presentacion">Presentación</li>
<li><a href="/contacto">Contacto</li>
<li><a href="/catalogo">Catalogo</li>
</ul>

"""

# Create your views here.
def home(request):
    return HttpResponse(html_cabecera+ "<h1>Proyecto</h1>")

def presentacion(request):
    return HttpResponse(html_cabecera+"<h1>Mi nombre es Gangale carlos</h1>")

def contacto(request):
    return HttpResponse(html_cabecera+"<h1>Numero telefonico 0987158210</h1>")

def catalogo(request):
    return HttpResponse(html_cabecera+"<h1>Productos</h1>")

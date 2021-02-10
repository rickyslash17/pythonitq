from django.shortcuts import render, HttpResponse

# Create your views here.
html_cabecera ="""
<h1>Welcome</h1>
<ul>
<li><a href="/">Home</li>
<li><a href="/presentacion">Presentación Producto</li>
</ul>

"""

# Create your views here.

def producto(request):
    return HttpResponse(html_cabecera+"<h1>Productos</h1>")

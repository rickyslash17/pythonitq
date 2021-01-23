from django.shortcuts import render, HttpResponse



# Create your views here.
def home(request):
    return render(request,"core/home.html")

def contacto(request):
    return render(request,"core/contacto.html")

def presentacion(request):
    return render(request,"core/presentacion.html")

def catalogo(request):
    return render(request,"core/catalogo.html")

def registro(request):
    return render(request,"core/registro.html")



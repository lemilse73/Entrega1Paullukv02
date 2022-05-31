from django.http import HttpResponse
from django.shortcuts import render
from app_running.models import Corredor
from django.template import loader
from app_running.forms import Corredor_formulario
from app_running.forms import Carreras_formulario
from app_running.models import Carreras
from app_running.forms import Teams_formulario
from app_running.models import Teams

# Create your views here.
def inicio (request):
    return render (request,"plantilla.html")


def corredor (request):
    corredor = Corredor.objects.all()
    dicc = {"corredor" : corredor}
    plantilla = loader.get_template ("corredor.html")
    documento = plantilla.render (dicc)
    return HttpResponse(documento)

def carreras (request):
    carreras = Carreras.objects.all()
    dicc = {"carreras" : carreras}
    plantilla = loader.get_template ("carreras.html")
    documento = plantilla.render (dicc)
    return HttpResponse(documento)

def teams (request):
    teams = Teams.objects.all()
    dicc = {"teams" : teams}
    plantilla = loader.get_template ("teams.html")
    documento = plantilla.render (dicc)
    return HttpResponse(documento)

def corredor_formulario(request):

    if request.method == "POST":

        mi_formulario = Corredor_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data


        corredor = Corredor( nombre = datos['nombre'] , apellido = datos['apellido'] , modalidad = datos['modalidad'] , email = datos['email'], team = datos['team'])
        corredor.save()
        return render(request , "formulario_corredor.html")

    return render (request, "formulario_corredor.html")

def carreras_formulario(request):

    if request.method == "POST":

        mi_formulario = Carreras_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data


        carreras = Carreras( nombre = datos['nombre'] , modalidad = datos['modalidad'] , distancia = datos['distancia'], fecha = datos['fecha'])
        carreras.save()
        return render(request , "formulario_carreras.html")

    return render (request, "formulario_carreras.html")

def teams_formulario(request):

    if request.method == "POST":

        mi_formulario = Teams_formulario( request.POST )
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data


        teams = Teams( nombre = datos['nombre'] , modalidad = datos['modalidad'] , email = datos['email'])
        teams.save()
        return render(request , "formulario_teams.html")

    return render (request, "formulario_teams.html")

def buscar_corredor(request):
    return render( request , "buscar_corredor.html")

def buscar(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        corredor = Corredor.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda.html", {"corredor": corredor})

    else:
        return HttpResponse(" Campo vacio")

def buscar_corredor_apellido(request):
    return render( request , "buscar_corredor_apellido.html")

def buscar_apellido(request):

    if request.GET['apellido']:
        apellido = request.GET['apellido']
        corredor = Corredor.objects.filter(apellido__icontains = apellido)
        return render( request , "resultado_busqueda_apellido.html", {"corredor": corredor})

    else:
        return HttpResponse(" Campo vacio")

def buscar_carreras_nombre(request):
    return render( request , "buscar_carreras_nombre.html")

def buscar_carreras(request):

    if request.GET['nombre']:
        nombre = request.GET['nombre']
        carreras = Carreras.objects.filter(nombre__icontains = nombre)
        return render( request , "resultado_busqueda_carreras.html", {"carreras": carreras})

    else:
        return HttpResponse(" Campo vacio")
# Create your views here.

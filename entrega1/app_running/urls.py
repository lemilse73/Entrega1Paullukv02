from django.urls import URLPattern, path 
from.import views

urlpatterns = [
    path ("", views.inicio),
    path ("corredor", views.corredor, name="corredor"),
    path ("carreras", views.carreras, name="carreras"),
    path ("teams", views.teams, name="teams"),
    path ("alta_corredor" , views.corredor_formulario),
    path ("alta_carreras" , views.carreras_formulario),
    path ("alta_teams" , views.teams_formulario),
    path ("buscar_corredor", views.buscar_corredor),
    path ("buscar", views.buscar),
    path ("buscar_corredor_apellido", views.buscar_corredor_apellido),
    path ("buscar_apellido", views.buscar_apellido),
    path ("buscar_carreras_nombre", views.buscar_carreras_nombre),
    path ("buscar_carreras", views.buscar_carreras)
]
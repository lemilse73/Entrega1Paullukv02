from django import forms


class Corredor_formulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    modalidad = forms.CharField(max_length=10)
    email = forms.EmailField()
    team = forms.CharField(max_length=10)

class Carreras_formulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    modalidad = forms.CharField(max_length=10)
    distancia= forms.IntegerField()
    fecha = forms.DateField()

class Teams_formulario(forms.Form):
    nombre = forms.CharField(max_length=20)
    modalidad = forms.CharField(max_length=10)
    email = forms.EmailField()

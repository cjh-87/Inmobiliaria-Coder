from django import forms

class PropietarioForm(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    telefono = forms.CharField(max_length=20)
    
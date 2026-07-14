from django import forms


class ClienteForm(forms.Form):

    nombre = forms.CharField(max_length=30)

    apellido = forms.CharField(max_length=30)

    email = forms.EmailField()

    telefono = forms.CharField(max_length=20)
    
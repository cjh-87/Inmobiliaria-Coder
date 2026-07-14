from django import forms
from propiedades.models import Propiedad


class PropiedadForm(forms.ModelForm):

    class Meta:
        model = Propiedad

        fields = [
            "titulo",
            "direccion",
            "localidad",
            "tipo",
            "ambientes",
            "precio",
            "estado",
            "propietario",
            "imagen",
        ]
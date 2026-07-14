from django.db import models

# Create your models here.
from django.db import models
from propietarios.models import Propietario


class Propiedad(models.Model):

    TIPOS = [
        ("Casa", "Casa"),
        ("Departamento", "Departamento"),
        ("PH", "PH"),
        ("Terreno", "Terreno"),
    ]

    ESTADOS = [
        ("Disponible", "Disponible"),
        ("Vendida", "Vendida"),
        ("Alquilada", "Alquilada"),
    ]


    titulo = models.CharField(max_length=100)

    direccion = models.CharField(max_length=150)

    localidad = models.CharField(max_length=100)

    tipo = models.CharField(
        max_length=50,
        choices=TIPOS
    )

    ambientes = models.IntegerField()

    precio = models.DecimalField(
        max_digits=12,
        decimal_places=2
    )

    imagen = models.ImageField(
        upload_to="propiedades/",
        blank=True,
        null=True
    )

    estado = models.CharField(
        max_length=50,
        choices=ESTADOS
    )

    propietario = models.ForeignKey(
        Propietario,
        on_delete=models.CASCADE
    )


    def __str__(self):
        return self.titulo
    
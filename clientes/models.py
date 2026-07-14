from django.db import models


class Cliente(models.Model):

    nombre = models.CharField(max_length=30)

    apellido = models.CharField(max_length=30)

    email = models.EmailField()

    telefono = models.CharField(max_length=20)


    def __str__(self):

        return f"{self.nombre} {self.apellido}"
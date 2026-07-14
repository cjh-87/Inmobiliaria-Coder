from django.urls import path

from .views import crear_propietario, listar_propietarios, eliminar_propietario, editar_propietario

urlpatterns = [

    path("", listar_propietarios, name="listar_propietarios"),

    path("crear/", crear_propietario, name="crear_propietario"),

    path("eliminar/<id>/", eliminar_propietario, name="eliminar_propietario"),

    path("editar/<id>/", editar_propietario, name="editar_propietario"),
]

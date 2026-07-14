from django.urls import path

from . import views


urlpatterns = [

    path(
        "",
        views.listar_propiedades,
        name="propiedades"
    ),


    path(
        "crear/",
        views.crear_propiedad,
        name="crear_propiedad"
    ),


    path(
        "editar/<int:id>/",
        views.editar_propiedad,
        name="editar_propiedad"
    ),


    path(
        "eliminar/<int:id>/",
        views.eliminar_propiedad,
        name="eliminar_propiedad"
    ),


    path(
        "detalle/<int:id>/",
        views.detalle_propiedad,
        name="detalle_propiedad"
    ),

]
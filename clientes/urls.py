from django.urls import path

from .views import crear_cliente, listar_clientes


urlpatterns = [

    path("", listar_clientes, name="listar_clientes"),

    path("crear/", crear_cliente, name="crear_cliente"),

]
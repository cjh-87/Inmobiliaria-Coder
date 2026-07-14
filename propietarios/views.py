from django.shortcuts import render, redirect

from propietarios.forms import PropietarioForm
from propietarios.models import Propietario

from django.contrib.auth.decorators import login_required


@login_required
def crear_propietario(request):

    if request.method == "POST":

        formulario = PropietarioForm(request.POST)

        if formulario.is_valid():

            datos = formulario.cleaned_data

            propietario = Propietario(
                nombre=datos["nombre"],
                apellido=datos["apellido"],
                telefono=datos["telefono"],
            )

            propietario.save()

            return redirect("inicio")

    else:

        formulario = PropietarioForm()

    return render(
        request,
        "propietarios/crear_propietario.html",
        {"form": formulario},
    )


def listar_propietarios(request):

    propietarios = Propietario.objects.all()

    return render(
        request,
        "propietarios/listar_propietarios.html",
        {"propietarios": propietarios}
    )

@login_required
def eliminar_propietario(request, id):

    propietario = Propietario.objects.get(id=id)

    propietario.delete()

    return redirect("listar_propietarios")

@login_required
def editar_propietario(request, id):

    propietario = Propietario.objects.get(id=id)

    if request.method == "POST":

        formulario = PropietarioForm(request.POST)

        if formulario.is_valid():

            datos = formulario.cleaned_data

            propietario.nombre = datos["nombre"]
            propietario.apellido = datos["apellido"]
            propietario.telefono = datos["telefono"]

            propietario.save()

            return redirect("listar_propietarios")

    else:

        formulario = PropietarioForm(
            initial={
                "nombre": propietario.nombre,
                "apellido": propietario.apellido,
                "telefono": propietario.telefono,
            }
        )

    return render(
        request,
        "propietarios/editar_propietario.html",
        {"form": formulario}
    )

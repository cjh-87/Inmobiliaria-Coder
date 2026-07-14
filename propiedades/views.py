from django.shortcuts import render, redirect, get_object_or_404
from propiedades.models import Propiedad
from propiedades.forms import PropiedadForm
from django.contrib.auth.decorators import login_required

def listar_propiedades(request):

    propiedades = Propiedad.objects.all()

    return render(
        request,
        "propiedades/listar_propiedades.html",
        {"propiedades": propiedades}
    )


@login_required
def crear_propiedad(request):

    if request.method == "POST":

        formulario = PropiedadForm(
            request.POST,
            request.FILES
)
        if formulario.is_valid():

            formulario.save()

            return redirect("propiedades")


    else:

        formulario = PropiedadForm()


    return render(
        request,
        "propiedades/crear_propiedad.html",
        {"form": formulario}
    )

@login_required
def editar_propiedad(request, id):

    propiedad = get_object_or_404(
        Propiedad,
        id=id
    )


    if request.method == "POST":

        formulario = PropiedadForm(
            request.POST,
            request.FILES,
            instance=propiedad
        )


        if formulario.is_valid():

            formulario.save()

            return redirect("propiedades")


    else:

        formulario = PropiedadForm(
            instance=propiedad
        )


    return render(
        request,
        "propiedades/editar_propiedad.html",
        {"form": formulario}
    )


@login_required
def eliminar_propiedad(request, id):

    propiedad = get_object_or_404(
        Propiedad,
        id=id
    )


    if request.method == "POST":

        propiedad.delete()

        return redirect("propiedades")


    return render(
        request,
        "propiedades/eliminar_propiedad.html",
        {"propiedad": propiedad}
    )

def detalle_propiedad(request, id):

    propiedad = Propiedad.objects.get(id=id)

    return render(
        request,
        "propiedades/detalle_propiedad.html",
        {"propiedad": propiedad}
    )
from django.shortcuts import render, redirect
from django.contrib import messages

from usuarios.forms import RegistroForm
from django.contrib.auth.decorators import login_required

from usuarios.models import UserProfile
from usuarios.forms import UserProfileForm

def registro(request):

    if request.method == "POST":

        formulario = RegistroForm(request.POST)

        if formulario.is_valid():

            formulario.save()

            messages.success(
                request,
                "Usuario creado correctamente. Ya podés iniciar sesión."
            )

            return redirect("login")

        else:

            messages.error(
                request,
                "No se pudo crear el usuario. Revisá los datos ingresados."
            )

    else:

        formulario = RegistroForm()

    return render(
        request,
        "usuarios/registro.html",
        {"form": formulario},
    )

@login_required
def editar_perfil(request):

    perfil = UserProfile.objects.get(user=request.user)

    if request.method == "POST":

        formulario = UserProfileForm(
            request.POST,
            request.FILES,
            instance=perfil
        )

        if formulario.is_valid():

            formulario.save()

            messages.success(
                request,
                "Perfil actualizado correctamente."
            )

            return redirect("editar_perfil")

    else:

        formulario = UserProfileForm(instance=perfil)

    return render(
    request,
    "usuarios/editar_perfil.html",
    {
        "form": formulario,
        "perfil": perfil,
    }
)
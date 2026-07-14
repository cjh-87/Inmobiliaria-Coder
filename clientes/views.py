from django.shortcuts import render, redirect

from clientes.forms import ClienteForm
from clientes.models import Cliente



def crear_cliente(request):

    if request.method == "POST":

        formulario = ClienteForm(request.POST)

        if formulario.is_valid():

            datos = formulario.cleaned_data

            cliente = Cliente(
                nombre=datos["nombre"],
                apellido=datos["apellido"],
                email=datos["email"],
                telefono=datos["telefono"],
            )

            cliente.save()

            return redirect("listar_clientes")


    else:

        formulario = ClienteForm()


    return render(
        request,
        "clientes/crear_cliente.html",
        {"form": formulario}
    )



def listar_clientes(request):

    clientes = Cliente.objects.all()


    return render(
        request,
        "clientes/listar_clientes.html",
        {"clientes": clientes}
    )

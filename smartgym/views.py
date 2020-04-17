from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *


# Views Authentication
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('principal')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('principal')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('principal')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


# Home View
@login_required(login_url='login')
def principal(request):
    context = {}
    return render(request, 'principal.html', context)


# Views para Empleados
@login_required(login_url='login')
def empleado_lista(request):
    context = {'empleado_lista': Empleado.objects.all()}
    return render(request, 'empleado_lista.html', context)


@login_required(login_url='login')
def empleado_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmpleadoForm()
        else:
            empleado = Empleado.objects.get(pk=id)
            form = EmpleadoForm(instance=empleado)
        return render(request, 'empleado_form.html', {'form': form})
    else:
        if id == 0:
            form = EmpleadoForm(request.POST)
        else:
            empleado = Empleado.objects.get(pk=id)
            form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
        return redirect('/empleado/lista')


@login_required(login_url='login')
def empleado_delete(request, id):
    empleado = Empleado.objects.get(pk=id)
    empleado.delete()
    return redirect('/empleado/lista')


# Views para Sucursales
@login_required(login_url='login')
def sucursal_lista(request):
    context = {'sucursal_lista': Sucursal.objects.all()}
    return render(request, 'sucursal_lista.html', context)


@login_required(login_url='login')
def sucursal_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = SucursalForm()
        else:
            sucursal = Sucursal.objects.get(pk=id)
            form = SucursalForm(instance=sucursal)
        return render(request, 'sucursal_form.html', {'form': form})
    else:
        if id == 0:
            form = SucursalForm(request.POST)
        else:
            sucursal = Sucursal.objects.get(pk=id)
            form = SucursalForm(request.POST, instance=sucursal)
        if form.is_valid():
            form.save()
        return redirect('/sucursal/lista')


# Views para Posibles Clientes
@login_required(login_url='login')
def cliente_lista(request):
    context = {'cliente_lista': PosibleCliente.objects.all()}
    return render(request, 'cliente_lista.html', context)


@login_required(login_url='login')
def cliente_form(request, id=0):
    if request.method == 'GET':
        if id == 0:
            form = PosibleClienteForm()
        else:
            cliente = PosibleCliente.objects.get(pk=id)
            form = PosibleClienteForm(instance=cliente)
        return render(request, 'cliente_form.html', {'form': form})
    else:
        if id == 0:
            form = PosibleClienteForm(request.POST)
        else:
            cliente = PosibleCliente.objects.get(pk=id)
            form = PosibleClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
        return redirect('/cliente/lista')

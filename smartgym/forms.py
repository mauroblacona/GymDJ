from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms


# Formulario registro usuario
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Formulario Empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        widgets = {'actividades': forms.widgets.CheckboxSelectMultiple()}
        fields = '__all__'
        labels = {
            'nombrecompleto': 'Nombre Completo'
        }

    def __init__(self, *args, **kwargs):
        super(EmpleadoForm, self).__init__(*args, **kwargs)
        self.fields['sucursal'].empty_label = '---------'
        #self.fields['status'].empty_label = 'Selecciona un status'
        # para excluir un campo y que no tenga validacion
        self.fields['observaciones_medicas'].required = False
        self.fields['email'].required = False
        self.fields['actividades'].required = False


# Formulario Sucursal
class SucursalForm(forms.ModelForm):
    class Meta:
        model = Sucursal
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(SucursalForm, self).__init__(*args, **kwargs)
        #self.fields['sucursal'].empty_label = 'Selecciona una sucursal'
        #self.fields['status'].empty_label = 'Selecciona un status'


# Formulario Posibles Clientes
class PosibleClienteForm(forms.ModelForm):
    class Meta:
        model = PosibleCliente
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(PosibleClienteForm, self).__init__(*args, **kwargs)
        #self.fields['sucursal'].empty_label = 'Selecciona una sucursal'
        #self.fields['status'].empty_label = 'Selecciona un status'

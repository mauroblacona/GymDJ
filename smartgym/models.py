from django.db import models
from model_utils import Choices


class Persona(models.Model):
    nombrecompleto = models.CharField(
        'Nombre y Apellido', max_length=120, null=True, blank=True)
    email = models.EmailField('Correo Electronico',
                              max_length=200, null=True, blank=True)
    dni = models.IntegerField('Documento', null=True, blank=True)
    GENEROS = Choices('Indefinido', 'Masculino', 'Femenino')
    genero = models.CharField(
        'Genero', null=True, max_length=50, blank=True, choices=GENEROS)
    telefono = models.CharField(
        'Telefono', null=True, max_length=50, blank=True)
    telefono_emergencia = models.CharField(
        'Telefono de Emergencia', null=True, max_length=50, blank=True)
    domicilio = models.CharField(
        'Domicilio', max_length=200, null=True, blank=True)
    fecha_nacimiento = models.DateField(
        'Fecha de Nacimiento', null=True, blank=True)
    fecha_inicio = models.DateField('Fecha de Inicio', null=True, blank=True)
    # foto = models.ImageField('Foto de Perfil', null=True,
    #                        blank=True, upload_to='imagenes/')

    class Meta:
        abstract = True


class Sucursal(models.Model):
    nombre = models.CharField('Nombre', max_length=120)
    direccion = models.CharField('Direccion', null=True, max_length=50)
    telefono = models.CharField('Telefono', null=True, max_length=50)
    encargado = models.CharField('Encargado', null=True, max_length=50)

    def __str__(self):
        return self.nombre


class Empleado(Persona):
    #ficha_medica = models.ImageField('Ficha Medica', null=True, blank=True)
    sucursal = models.ForeignKey(
        Sucursal, on_delete=models.CASCADE, null=True, blank=True)
    especialidad = models.CharField(
        'Especialidad', max_length=200, null=True, blank=True)
    observaciones_medicas = models.TextField(
        'Observaciones Medicas', blank=True, null=True)
    actividades = models.ManyToManyField('Actividad', blank=True)
    ACTIVO, INACTIVO = ('Activo', 'Inactivo')
    STATUSES = ((ACTIVO, 'Activo'), (INACTIVO, 'Inactivo'),)
    status = models.CharField(
        choices=STATUSES, null=True, blank=True, max_length=150)

    def __str__(self):
        return self.nombrecompleto


class Actividad(models.Model):
    nombre = models.CharField('Nombre', max_length=150)
    capacidad = models.IntegerField('Capacidad', blank=True, null=True)
    empleados = models.ManyToManyField('Empleado', blank=True)
    sucursal = models.ForeignKey(
        Sucursal, on_delete=models.CASCADE, null=True, blank=True)
    precio = models.IntegerField('Precio', null=True, blank=True)

    def __str__(self):
        return self.nombre


class PosibleCliente(models.Model):
    nombrecompleto = models.CharField(
        'Nombre y Apellido', max_length=120, null=True, blank=True)
    email = models.EmailField('Correo Electronico', blank=True, null=True)
    fecha_consulta = models.DateField(
        'Fecha de Consulta', null=True, blank=True)
    actividad = models.TextField('Actividad Consultada', null=True, blank=True)

    def __str__(self):
        return self.nombrecompleto

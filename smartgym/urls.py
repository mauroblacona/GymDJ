from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    # Empleados
    path('empleado/', views.empleado_form, name='empleado_insert'),
    path('empleado/<int:id>/', views.empleado_form, name='empleado_update'),
    path('delete/<int:id>/', views.empleado_delete, name='empleado_delete'),
    path('empleado/lista', views.empleado_lista, name='empleado_lista'),
    # Sucursales
    path('sucursal/', views.sucursal_form, name='sucursal_insert'),
    path('sucursal/<int:id>/', views.sucursal_form, name='sucursal_update'),
    path('sucursal/lista', views.sucursal_lista, name='sucursal_lista'),
    # Posibles Clientes
    path('cliente/', views.cliente_form, name='cliente_insert'),
    path('cliente/<int:id>/', views.cliente_form, name='cliente_update'),
    path('cliente/lista', views.cliente_lista, name='cliente_lista'),
]

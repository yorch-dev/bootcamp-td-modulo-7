from django.urls import path
from . import views

urlpatterns = [
    path("", views.crud_lab, name="crud_lab"),
    path("actualizar/<int:pk>", views.ActualizarLaboratorio.as_view(), name="crud_lab_actualizar"),
    path("eliminar/<int:pk>", views.EliminarLaboratorio.as_view(), name="crud_lab_eliminar"),
    path("crear/", views.CrearLaboratorio.as_view(), name="crud_lab_insertar"),
]

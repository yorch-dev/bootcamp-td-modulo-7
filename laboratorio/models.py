from django.db import models
from django.core.validators import MinValueValidator
import datetime as dt

# Create your models here.
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50, default='No informada')
    pais = models.CharField(max_length=50, default='No informado')

    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=50)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.SET_NULL, blank=True, null=True)
    especialidad = models.CharField(max_length=50, default='No informada')


    class Meta:
        verbose_name = 'Director general'
        verbose_name_plural = 'Directores generales'

    def __str__(self):
        return f"{self.nombre}, {self.laboratorio}"

class Producto(models.Model):
    fecha_minima = dt.date(2015, 1, 1)
    nombre = models.CharField(max_length=50)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.SET_NULL, blank=True, null=True)
    f_fabricacion = models.DateField(auto_now=False, auto_now_add=False, validators=[MinValueValidator(fecha_minima, 'Fecha mínima: año 2015')], default=fecha_minima)
    p_costo = models.DecimalField(max_digits=10, decimal_places=2)
    p_venta = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.nombre}, {self.laboratorio}, precio venta: {self.p_venta}"

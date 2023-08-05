from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    list_display_links = ('id', 'nombre')

class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    list_display_links = ('id', 'nombre', 'laboratorio')

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'p_costo', 'p_venta')
    list_filter = ('nombre', 'laboratorio')
    list_display_links = ('nombre', 'laboratorio')

    def f_fabricacion_year(self, obj):
        return obj.f_fabricacion.year

    f_fabricacion_year.short_description = 'F Fabricacion'

    list_display = list(list_display)
    list_display.insert(list_display.index('p_costo'), 'f_fabricacion_year')

admin.site.register(Laboratorio, LaboratorioAdmin)
admin.site.register(DirectorGeneral, DirectorGeneralAdmin)
admin.site.register(Producto, ProductoAdmin)
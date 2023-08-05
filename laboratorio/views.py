from django.shortcuts import render
from .models import Laboratorio
from django.views.generic import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

# Create your views here.
def crud_lab(request):
    laboratorios = Laboratorio.objects.all()
    visitas = request.session.get('visitas', 0)
    visitas += 1
    request.session['visitas'] = visitas
    ctx = {
        'laboratorios' : laboratorios,
        'visitas' : visitas,
    }
    return render(request, 'app_laboratorio/laboratorio.html', ctx)


class ActualizarLaboratorio(UpdateView):
    success_url = reverse_lazy('crud_lab')
    model = Laboratorio
    template_name = 'app_laboratorio/form_laboratorio.html'
    fields = ['nombre', 'ciudad', 'pais']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Actualizar laboratorio'
        return context

class EliminarLaboratorio(DeleteView):
    success_url = reverse_lazy('crud_lab')
    model = Laboratorio
    template_name = 'app_laboratorio/borrar_laboratorio.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Eliminar laboratorio'
        return context

class CrearLaboratorio(CreateView):
    success_url = reverse_lazy('crud_lab')
    model = Laboratorio
    template_name = 'app_laboratorio/crear_laboratorio.html'
    fields = ['nombre', 'ciudad', 'pais']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nombre'] = 'Crear laboratorio'
        return context
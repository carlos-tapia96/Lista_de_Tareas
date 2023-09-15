from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Task
from django.urls import reverse_lazy

# Create your views here.
class ListaPendientes(ListView):
    model = Task
    context_object_name = 'tareas'
    template_name = 'base/tarea_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tareas"] = context ['tareas'].filter(user=self.request.user)
        context["count"] = context ['tareas'].filter(completed=False).count()

        valor_buscado = self.request.GET.get('area-buscar') or ''
        if valor_buscado:
            context['tareas'] = context['tareas'].filter(tittle__icontains=valor_buscado)
            context['valor_buscado'] = valor_buscado
        return context

class DetalleTarea(DetailView):
    model = Task
    context_object_name = 'tarea'
    template_name = 'base/tarea.html'

class CrearTarea(CreateView):
    model = Task
    fields = ['tittle', 'description', 'completed']
    success_url = reverse_lazy('tareas')
    template_name = 'base/tarea_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CrearTarea, self).form_valid(form)


class EditarTarea(UpdateView):
    model = Task
    fields = ['tittle', 'description', 'completed']
    success_url = reverse_lazy('tareas')
    template_name = 'base/tarea_form.html'

class EliminarTarea(DeleteView):
    model = Task
    context_object_name = 'tarea'
    success_url = reverse_lazy('tareas')
    template_name = 'base/tarea_delete.html'







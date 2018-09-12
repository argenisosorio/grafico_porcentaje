# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Actividad


class Consultar(ListView):
    model = Actividad


class Registrar(CreateView):
    model = Actividad
    fields = ['nombre', 'avance']
    success_url = reverse_lazy('registro:consultar')


class Editar(UpdateView):
    model = Actividad
    fields = ['nombre', 'avance']
    success_url = reverse_lazy('registro:consultar')


class Borrar(DeleteView):
    model = Actividad
    success_url = reverse_lazy('registro:consultar')

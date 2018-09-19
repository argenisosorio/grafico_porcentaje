# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Proyecto


class Consultar(ListView):
    model = Proyecto


class Registrar(CreateView):
    model = Proyecto
    fields = ['nombre', 'avance']
    success_url = reverse_lazy('registro:consultar')


class Editar(UpdateView):
    model = Proyecto
    fields = ['nombre', 'avance']
    success_url = reverse_lazy('registro:consultar')


class Borrar(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('registro:consultar')

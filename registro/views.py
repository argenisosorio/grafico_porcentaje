# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from registro.models import Proyecto
from forms import ProyectoForm


##################################################
##### CRUD de la Gestión básica de Proyectos #####
##################################################

class Consultar(ListView):
    """
    Clase que permite listar los proyectos.
    """
    model = Proyecto


class Registrar(CreateView):
    """
    Clase que permite registrar un proyecto.
    """
    model = Proyecto
    form_class = ProyectoForm
    success_url = reverse_lazy('registro:consultar')


class Registrar_software(CreateView):
    """
    Clase que permite registrar un proyecto de tipo Software.
    """
    model = Proyecto
    template_name = "registro/proyecto_software_form.html"
    form_class = ProyectoForm
    success_url = reverse_lazy('registro:consultar')


class Editar(UpdateView):
    """
    Clase que permite editar los datos de un proyecto registrado.
    """
    model = Proyecto
    form_class = ProyectoForm
    success_url = reverse_lazy('registro:consultar')


class Borrar(DeleteView):
    """
    Clase que borrar un proyecto registrado.
    """
    model = Proyecto
    success_url = reverse_lazy('registro:consultar')

class Detallar(DetailView):
    """
    Clase que muestra la lista de entradas de la bitácora
    """
    model = Proyecto
    template_name = "registro/proyecto_detail.html"

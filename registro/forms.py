# -*- coding: utf-8 -*-
from django import forms
from registro.models import Proyecto
from django.forms import (
    TextInput, CharField, Select, RadioSelect, Textarea, CheckboxInput, DateTimeField
)


class ProyectoForm(forms.ModelForm):
    """
    Formulario que maneja los campos de un Proyecto.
    """
    nombre = forms.CharField(label='Nombre del Proyecto', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    actividad_1 = forms.CharField(label='Actividad 1 %', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
        'value':'0',
    }), required = True)

    actividad_2 = forms.CharField(label='Actividad 2 %', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
        'value':'0',
    }), required = True)

    class Meta:

        model = Proyecto
        fields = '__all__'

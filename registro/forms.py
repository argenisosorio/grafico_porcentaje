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
    nombre_proyecto = forms.CharField(label='Nombre del Proyecto', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    nombre_caravisible = forms.CharField(label='Nombre del Cara Visible', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    nombre_director = forms.CharField(label='Nombre del Director', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
        'required': 'True',
    }), required = True)

    # Nombres de las actividades del proyecto.
    nombre_act_1 = forms.CharField(label='Nombre de la Actividad 1', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_2 = forms.CharField(label='Nombre de la Actividad 2', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_3 = forms.CharField(label='Nombre de la Actividad 3', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_4 = forms.CharField(label='Nombre de la Actividad 4', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_5 = forms.CharField(label='Nombre de la Actividad 5', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_6 = forms.CharField(label='Nombre de la Actividad 6', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_7 = forms.CharField(label='Nombre de la Actividad 7', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_8 = forms.CharField(label='Nombre de la Actividad 8', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_9 = forms.CharField(label='Nombre de la Actividad 9', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    nombre_act_10 = forms.CharField(label='Nombre de la Actividad 10', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Fechas de entrega de las actividades del proyecto.
    fecha_entrega_act_1 = forms.CharField(label='Fecha de entrega de la Actividad 1', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_2 = forms.CharField(label='Fecha de entrega de la Actividad 2', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_3 = forms.CharField(label='Fecha de entrega de la Actividad 3', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_4 = forms.CharField(label='Fecha de entrega de la Actividad 4', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_5 = forms.CharField(label='Fecha de entrega de la Actividad 5', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_6 = forms.CharField(label='Fecha de entrega de la Actividad 6', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_7 = forms.CharField(label='Fecha de entrega de la Actividad 7', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_8 = forms.CharField(label='Fecha de entrega de la Actividad 8', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_9 = forms.CharField(label='Fecha de entrega de la Actividad 9', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    fecha_entrega_act_10 = forms.CharField(label='Fecha de entrega de la Actividad 10', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Porcentaje de las actividades del proyecto.
    porc_act_1 = forms.CharField(label='Porcentaje de la Actividad 1', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_2 = forms.CharField(label='Porcentaje de la Actividad 2', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_3 = forms.CharField(label='Porcentaje de la Actividad 3', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_4 = forms.CharField(label='Porcentaje de la Actividad 4', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_5 = forms.CharField(label='Porcentaje de la Actividad 5', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_6 = forms.CharField(label='Porcentaje de la Actividad 6', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_7 = forms.CharField(label='Porcentaje de la Actividad 7', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_8 = forms.CharField(label='Porcentaje de la Actividad 8', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_9 = forms.CharField(label='Porcentaje de la Actividad 9', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_act_10 = forms.CharField(label='Porcentaje de la Actividad 10', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    # Porcentaje de avance de las actividades del proyecto.
    porc_avan_act_1 = forms.CharField(label='Porcentaje de avance la Actividad 1', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_avan_act_2 = forms.CharField(label='Porcentaje de avance la Actividad 2', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_avan_act_3 = forms.CharField(label='Porcentaje de avance la Actividad 3', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_avan_act_4 = forms.CharField(label='Porcentaje de avance la Actividad 4', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_avan_act_5 = forms.CharField(label='Porcentaje de avance la Actividad 5', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_avan_act_6 = forms.CharField(label='Porcentaje de avance la Actividad 6', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_avan_act_7 = forms.CharField(label='Porcentaje de avance la Actividad 7', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_avan_act_8 = forms.CharField(label='Porcentaje de avance la Actividad 8', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_avan_act_9 = forms.CharField(label='Porcentaje de avance la Actividad 9', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    porc_avan_act_10 = forms.CharField(label='Porcentaje de avance la Actividad 10', widget=TextInput(attrs={
        'class':'form-control input-md',
        'style': 'min-width: 0; width: 100%; display: inline;',
    }), required = False)

    class Meta:

        model = Proyecto
        fields = '__all__'

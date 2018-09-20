# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Proyecto(models.Model):
    """
    Modelo que contiene los campos de un Proyecto.
    """
    nombre = models.CharField(max_length=200)
    actividad_1 = models.IntegerField()
    actividad_2 = models.IntegerField()

    def total(self):
        """
        Función que suma los porcentajes de cada actividad
        y retorna el total de la operación.
        """
        total = self.actividad_1+self.actividad_2
        return total

    def __unicode__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('registro:editar', kwargs={'pk': self.pk})

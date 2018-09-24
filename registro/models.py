# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Proyecto(models.Model):
    """
    Modelo que contiene los campos de un Proyecto.
    """
    nombre_proyecto = models.CharField(max_length=4000, blank=True,null=True)
    nombre_caravisible = models.CharField(max_length=4000, blank=True,null=True)
    nombre_director = models.CharField(max_length=4000, blank=True,null=True)
    # Nombres de las actividades del proyecto.
    nombre_act_1 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_2 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_3 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_4 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_5 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_6 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_7 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_8 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_9 = models.CharField(max_length=4000, blank=True,null=True)
    nombre_act_10 = models.CharField(max_length=4000, blank=True,null=True)
    # Fechas de entrega de las actividades del proyecto.
    fecha_entrega_act_1 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_2 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_3 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_4 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_5 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_6 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_7 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_8 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_9 = models.CharField(max_length=100, blank=True,null=True)
    fecha_entrega_act_10 = models.CharField(max_length=100, blank=True,null=True)
    # Porcentaje de las actividades del proyecto.
    porc_act_1 = models.CharField(max_length=100, blank=True,null=True)
    porc_act_2 = models.CharField(max_length=100, blank=True,null=True)
    porc_act_3 = models.CharField(max_length=100, blank=True,null=True)
    porc_act_4 = models.CharField(max_length=100, blank=True,null=True)
    porc_act_5 = models.CharField(max_length=100, blank=True,null=True)
    porc_act_6 = models.CharField(max_length=100, blank=True,null=True)
    porc_act_7 = models.CharField(max_length=100, blank=True,null=True)
    porc_act_8 = models.CharField(max_length=100, blank=True,null=True)
    porc_act_9 = models.CharField(max_length=100, blank=True,null=True)
    porc_act_10 = models.CharField(max_length=100, blank=True,null=True)
    # Porcentaje de avance de las actividades del proyecto.
    porc_avan_act_1 = models.IntegerField()
    porc_avan_act_2 = models.IntegerField()
    porc_avan_act_3 = models.IntegerField()
    porc_avan_act_4 = models.IntegerField()
    porc_avan_act_5 = models.IntegerField()
    porc_avan_act_6 = models.IntegerField()
    porc_avan_act_7 = models.IntegerField()
    porc_avan_act_8 = models.IntegerField()
    porc_avan_act_9 = models.IntegerField()
    porc_avan_act_10 = models.IntegerField()

    def sumatoria_por_avan(self):
        sumatoria_por_avan = self.porc_avan_act_1+self.porc_avan_act_2+self.porc_avan_act_3+self.porc_avan_act_4+self.porc_avan_act_5+self.porc_avan_act_6+self.porc_avan_act_7+self.porc_avan_act_8+self.porc_avan_act_9+self.porc_avan_act_10
        return sumatoria_por_avan

    def __unicode__(self):
        return self.nombre_proyecto

    def get_absolute_url(self):
        return reverse('registro:editar', kwargs={'pk': self.pk})

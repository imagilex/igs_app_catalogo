from django.db import models

from igs_app_base.utils.utils import absolute_url


class TipoParametro(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    tipo_interno = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ['nombre']
        unique_together = [['nombre', 'tipo_interno']]

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return absolute_url(self)

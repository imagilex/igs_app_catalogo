from django.db import models

from igs_app_base.utils.utils import absolute_url


class BootstrapColor(models.Model):
    nombre = models.CharField(max_length=50)
    clase_color = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ["nombre"]

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return absolute_url(self)

    @property
    def text_class(self):
        return f"text-{self.clase_color}"

    @property
    def bg_class(self):
        return f"bg-{self.clase_color}"

    @property
    def border_class(self):
        return f"border-{self.clase_color}"

    @property
    def alert_class(self):
        return f"alert alert--{self.clase_color}"

    @property
    def btn_class(self):
        return f"btn btn-{self.clase_color}"

    @property
    def btn_outline_class(self):
        return f"btn btn-outline-{self.clase_color}"

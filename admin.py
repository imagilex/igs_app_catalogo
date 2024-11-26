from django.contrib import admin

from .models import BootstrapColor
from .models import TipoParametro


@admin.register(TipoParametro)
class TipoParametroAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo_interno')


@admin.register(BootstrapColor)
class BootstrapColorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'clase_color')

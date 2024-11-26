from igs_app_base.views import GenericViews

from .forms import MainForm
from .models import TipoParametro

views = GenericViews(
    TipoParametro, "Tipo de Parámetro", "Tipos de Parámetro",
    "catalogo", MainForm, MainForm, MainForm)

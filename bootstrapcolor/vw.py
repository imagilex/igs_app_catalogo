from igs_app_base.views import GenericViews

from .forms import MainForm
from .models import BootstrapColor

views = GenericViews(
    BootstrapColor, "Color Bootstrap", "Colores Bootstrap",
    "catalogo", MainForm, MainForm, MainForm)

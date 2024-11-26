from igs_app_base.hiperforms import BaseHiperModelForm

from .models import TipoParametro


class MainForm(BaseHiperModelForm):

    class Meta:
        model = TipoParametro
        fields = "__all__"

from igs_app_base.hiperforms import BaseHiperModelForm

from .models import BootstrapColor


class MainForm(BaseHiperModelForm):

    class Meta:
        model = BootstrapColor
        fields = "__all__"

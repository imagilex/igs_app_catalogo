from django.contrib.auth.decorators import login_required
from django.urls import include
from django.urls import path

from .views import Catalogos

urlpatterns = [
    path('tipo-parametro/', include('igs_app_catalogo.tipoparametro.urls')),
    path('color-bootstrap/', include('igs_app_catalogo.bootstrapcolor.urls')),

    path(
        'catalogos-de-sistema/',
        login_required()(Catalogos.as_view()),
        name="idx_app_catalogo"),
    ]

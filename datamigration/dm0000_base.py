from igs_app_base.menu.models import MenuOpc
from igs_app_base.models import App
from igs_app_base.utils.utils import add_or_create_menuopc
from igs_app_catalogo.models import BootstrapColor
from igs_app_catalogo.models import TipoParametro


def migration():
    app, created = App.objects.get_or_create(nombre="catalogo")
    if created:
        app.posicion = 75
        app.save()

    cat = MenuOpc.objects.get_or_create(
        nombre="Catalogos", posicion=75, vista='idx_app_catalogo')[0]

    subopcion = MenuOpc.objects.get_or_create(
        nombre="Generales", posicion=100, padre=cat)[0]

    add_or_create_menuopc(
        "Colores Bootstrap", 1,
        subopcion, "bootstrapcolor")
    add_or_create_menuopc(
        "Tipos de Parametro", 2,
        subopcion, "tipoparametro")

    TipoParametro.objects.get_or_create(
        nombre="Entero", tipo_interno="INTEGER")
    TipoParametro.objects.get_or_create(
        nombre="Cadena", tipo_interno="STRING")
    TipoParametro.objects.get_or_create(
        nombre="Texto Largo", tipo_interno="TEXT")
    TipoParametro.objects.get_or_create(
        nombre="Imagen", tipo_interno="PICTURE")
    TipoParametro.objects.get_or_create(
        nombre="Archivo", tipo_interno="FILE")
    TipoParametro.objects.get_or_create(
        nombre="Decimal", tipo_interno="DECIMAL")

    BootstrapColor.objects.get_or_create(
        nombre="Primary", clase_color="primary")
    BootstrapColor.objects.get_or_create(
        nombre="Secondary", clase_color="secondary")
    BootstrapColor.objects.get_or_create(
        nombre="Success", clase_color="success")
    BootstrapColor.objects.get_or_create(
        nombre="Danger", clase_color="danger")
    BootstrapColor.objects.get_or_create(
        nombre="Warning", clase_color="warning")
    BootstrapColor.objects.get_or_create(
        nombre="Info", clase_color="info")
    BootstrapColor.objects.get_or_create(
        nombre="Light", clase_color="light")
    BootstrapColor.objects.get_or_create(
        nombre="Dark", clase_color="dark")
    BootstrapColor.objects.get_or_create(
        nombre="Body", clase_color="body")
    BootstrapColor.objects.get_or_create(
        nombre="Muted", clase_color="muted")
    BootstrapColor.objects.get_or_create(
        nombre="White", clase_color="white")

from .vw import views

obj = 'bootstrapcolor'
app_label = 'igs_app_catalogo'

urlpatterns = views.create_urls(app_label)

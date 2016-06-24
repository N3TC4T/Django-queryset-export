from django.conf.urls import url

from .views import ExporterView


urlpatterns = [
    url(
        regex=r'^export/$',
        view=ExporterView,
        name='exporter',
    ),
]
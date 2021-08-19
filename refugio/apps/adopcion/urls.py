from django.conf.urls import url,include

from refugio.apps.adopcion.views import index_adopcion


urlpatterns = [
    url(r'^index$', index_adopcion),
]
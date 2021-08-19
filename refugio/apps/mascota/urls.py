from django.conf.urls import url,include

from refugio.apps.mascota.views import create, index


urlpatterns = [
    url(r'^$', index, name="index"),
    url(r'^crear/$', create,name="create"),
    url(r'^store/$', create,name="store"),
    
]
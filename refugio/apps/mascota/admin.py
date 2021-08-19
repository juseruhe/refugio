from django.contrib.admin.decorators import register
from refugio.apps.mascota.models import Mascota, Vacuna
from django.contrib import admin

from refugio.apps.mascota.models import Mascota,Vacuna

# Register your models here.

admin.site.register(Mascota)
admin.site.register(Vacuna)
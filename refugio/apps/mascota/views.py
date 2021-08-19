from refugio.apps.mascota.forms import MascotaForm
from django.shortcuts import redirect, render
from refugio.apps.mascota.models import Mascota
from django.http import HttpResponse, response

# Create your views here.


def index(request):
    mascotas = Mascota.objects.all()
    datos = {
        "mascotas": mascotas
    }
    return render(request,"mascota/index.html",datos)

def create(request):
    mascota = MascotaForm()
    form = {'form': mascota}
    return render(request,"mascota/mascota_form.html",form)

def store(request):
    form = MascotaForm(request.POST)
    if form.is_valid():
        form.save()
    return redirect('index')
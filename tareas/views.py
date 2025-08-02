from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import Formulario_Tarea

# Create your views here.


@login_required
def tareas(request):
    return render(request, "tareas.html", {})

def crear_tarea(request):
    return render(request, "crear_tarea.html", {"form": Formulario_Tarea})
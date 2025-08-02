from django.urls import path
from .views import tareas, crear_tarea

urlpatterns = [
    path("tareas/", tareas, name="tareas"),
    path("crear_tarea/", crear_tarea, name="crear_tarea"),
]


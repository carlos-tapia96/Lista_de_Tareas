from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea,EditarTarea,EliminarTarea


urlpatterns = [
    path('', ListaPendientes.as_view(), name="tareas"),
    path('tarea/<int:pk>', DetalleTarea.as_view(), name="tarea"),
    path('crear-tarea/>', CrearTarea.as_view(), name="crear-tarea"),
    path('editar-tarea/<int:pk>>', EditarTarea.as_view(), name="editar-tarea"),
    path('eliminar-tarea/<int:pk>>', EliminarTarea.as_view(), name="eliminar-tarea"),


]



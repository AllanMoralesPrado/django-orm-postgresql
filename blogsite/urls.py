from django.urls import path
from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.Index.as_view(), name='index'),
    path('agregar/', views.agregar, name='agregar'),
    path('agregar/agregarregistro/', views.agregarregistro, name='agregarregistro'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('actualizar/<int:id>', views.actualizar, name='actualizar'), 
    path('actualizar/actualizarregistro/<int:id>', views.actualizarregistro, name='actualizarregistro')
]
from django.urls import path
from . import views

urlpatterns = [

    path('', views.listar_alumno,name='listar_alumno'),
    path('insertar/', views.insertar_alumno,name='insertar_alumno'),
    path('editar/<int:id_alumno>/',views.editar_alumno,name='editar_alumno'),
    path('eliminar/<int:id_alumno>/',views.eliminar_alumno,name='eliminar_alumno'),

]
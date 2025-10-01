from django.urls import path
from . import views

urlpatterns = [
    path('agregar/', views.agregar_contacto, name='agregar_contacto'),
    path('listar/', views.listar_contactos, name='listar_contactos'),
    path('buscar/', views.buscar_contactos, name='buscar_contactos'),
    path('eliminar/<int:contacto_id>/', views.eliminar_contacto, name='eliminar_contacto'),
]
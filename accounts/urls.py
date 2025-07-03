from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.iniciar_sesion, name='login'),
    path('logout/', views.cerrar_sesion, name='logout'),
    path('signup/', views.registro, name='signup'),
    path('profile/', views.perfil, name='profile'),
    path('profile/edit/', views.editar_perfil, name='editar_perfil'),
    path('profile/password/', views.cambiar_password, name='cambiar_password'),
]

from django.urls import path
from accounts.views import perfil_view, cambiar_perfil_view ,actualizar_contrasenia, borrar_imagen

urlpatterns = [
    path('', perfil_view),
    path('profile/', cambiar_perfil_view, name="cambiar datos"),
    path('profile/cambiar-clave', actualizar_contrasenia, name="cambiar clave"),
    path('profile/borrar-imagen', borrar_imagen, name="borrar imagen"),
]

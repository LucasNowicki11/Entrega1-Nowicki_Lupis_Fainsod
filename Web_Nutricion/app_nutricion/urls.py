from django.urls import path
from app_nutricion.views import listar_clientes, evaluacion_antropometrica, cargar_clientes, cargar_receta, recetas, cargar_evaluacion, search_client_view, detail_cliente, delete_cliente, edit_cliente, agregar_avatar

urlpatterns = [
    path('',listar_clientes, name='lista_clientes'),
    path('evaluacion/', evaluacion_antropometrica, name="evaluacion_antropometrica"),
    path('cargar-clientes/', cargar_clientes, name='cargar_clientes'),
    path('recetas/', recetas, name='recetas'),
    path('cargar-evaluacion/',cargar_evaluacion, name='cargar_evaluacion'),
    path('cargar-receta/',cargar_receta, name='cargar_receta'),
    path('search-client/', search_client_view, name='search_client'),
    path('agregar-avatar/', agregar_avatar, name='agregar avatar'),
    path('detail-cliente/<int:pk>/', detail_cliente, name='detail_cliente'),
    path('delete-cliente/<int:pk>/', delete_cliente, name='delete_cliente'),
    path('edit-cliente/<int:id>/', edit_cliente, name='edit_cliente'),
]

from django.urls import path

from . import views


urlpatterns = [

    path(
        'obras/',
        views.ListarCriarObras.as_view()
    ),

    path(
        'obras/<int:pk>/',
        views.GerenciarObra.as_view()
    ),

    path(
        'obras/artista/<str:nome>/',
        views.obras_por_artista
    ),


    path(
        'obras/movimento/<str:nome>/',
        views.obras_por_movimento
    ),

    path(
        'obras/museu/<str:nome>/',
        views.obras_por_museu
    ),

    path(
        'obras/ano/<int:ano>/',
        views.obras_por_ano
    ),

    path(
        'obras/buscar/',
        views.buscar_obra
    ),

]
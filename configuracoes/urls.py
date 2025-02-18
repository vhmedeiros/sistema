from django.urls import path
from . import views


urlpatterns = [
    path('cliente/<int:id_cliente>/palavras-chave/', views.ClientePalavrasChaveListView.as_view(), name='cliente_palavras_chave_list'),
    path('cliente/<int:id_cliente>/noticias/', views.ClienteNoticiasListView.as_view(), name='cliente_noticias_list'),
    path('categorias/list/', views.CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/create/', views.CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/detail/', views.CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categorias/<int:pk>/update/', views.CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/delete/', views.CategoriaDeleteView.as_view(), name='categoria_delete'),
    path('palavras-chave/list/', views.PalavraChaveListView.as_view(), name='palavra_chave_list'),
    path('palavras-chave/create/', views.PalavraChaveCreateView.as_view(), name='palavra_chave_create'),
    path('palavras-chave/<int:pk>/detail/', views.PalavraChaveDetailView.as_view(), name='palavra_chave_detail'),
    path('palavras-chave/<int:pk>/update/', views.PalavraChaveUpdateView.as_view(), name='palavra_chave_update'),
    path('palavras-chave/<int:pk>/delete/', views.PalavraChaveDeleteView.as_view(), name='palavra_chave_delete'),
]
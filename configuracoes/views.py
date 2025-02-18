from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Categoriapalavrachave, Palavrachave
from .forms import CategoriaPalavraChaveForm, PalavraChaveForm
from clientes.models import ErpCliente
from noticias.models import NoticiaImportada

# view para as PC do cliente


class ClientePalavrasChaveListView(ListView):
    model = Categoriapalavrachave
    template_name = 'cliente_palavra_chave_list.html'
    context_object_name = 'categorias'

    def get_queryset(self):
        """
        Filtra as categorias de palavras-chave do cliente selecionado.
        """
        id_cliente = self.kwargs.get(
            'id_cliente')  # 🔹 Alterado para "id_cliente"
        self.cliente = get_object_or_404(ErpCliente, id_cliente=id_cliente)
        return Categoriapalavrachave.objects.filter(palavrachave__id_cliente=self.cliente).distinct()

    def get_context_data(self, **kwargs):
        # pega o cliente e adiciona ao contexto
        context = super().get_context_data(**kwargs)
        context['cliente'] = self.cliente
        return context

# view para as notícias do cliente
# class ClienteNoticiasListView(ListView):
#     model = NoticiaImportada
#     template_name = 'cliente_noticias_list.html'  
#     context_object_name = 'noticias'
#     paginate_by = 20  

#     def get_queryset(self):
#         id_cliente = self.kwargs.get('id_cliente')
#         return NoticiaImportada.objects.filter(
#             clientes_relacionados__contains=str(id_cliente)
#         ).order_by('-dt_noticia')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         id_cliente = self.kwargs.get('id_cliente')
#         cliente = get_object_or_404(ErpCliente, id_cliente=id_cliente)
#         noticias = self.get_queryset()

#         # Mapeamento de tipos de veículos
#         tipos_veiculo_mapeados = {
#             'Impresso': 'Impresso',
#             'Jornal': 'Impresso',
#             'Revista': 'Revista',
#             'Site': 'Site',
#             'Portal': 'Site',
#             'Blog': 'Blog',
#             'Podcast': 'Podcast',
#             'Rádio': 'Rádio',
#             'Televisão': 'Televisão',
#             'Videocast': 'Videocast'
#         }

#         # Dicionário para agrupar as notícias
#         noticias_por_tipo = {tipo: [] for tipo in tipos_veiculo_mapeados.values()}

#         for noticia in noticias:
#             if noticia.cd_veiculo and noticia.cd_veiculo.tipo_veiculo:
#                 tipo_veiculo = noticia.cd_veiculo.tipo_veiculo.descricao_tipo_veiculo
#                 print(f"Tipo de veículo retornado do banco: {tipo_veiculo}")  

#                 tipo_veiculo = tipos_veiculo_mapeados.get(tipo_veiculo, 'Outros')

#                 if tipo_veiculo not in noticias_por_tipo:
#                     noticias_por_tipo[tipo_veiculo] = []
#                 noticias_por_tipo[tipo_veiculo].append(noticia)

#         context['cliente'] = cliente
#         context['noticias_por_tipo'] = noticias_por_tipo
#         return context

class ClienteNoticiasListView(ListView):
    model = NoticiaImportada
    template_name = 'cliente_noticias_list.html'  
    context_object_name = 'noticias'
    paginate_by = 20  

    def get_queryset(self):
        id_cliente = self.kwargs.get('id_cliente')
        return NoticiaImportada.objects.filter(
            clientes_relacionados__contains=str(id_cliente)
        ).order_by('-dt_noticia')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id_cliente = self.kwargs.get('id_cliente')
        cliente = get_object_or_404(ErpCliente, id_cliente=id_cliente)
        noticias = self.get_queryset()

        # Criar um dicionário para armazenar todas as notícias agrupadas corretamente
        noticias_por_tipo = {}

        for noticia in noticias:
            if noticia.cd_veiculo and noticia.cd_veiculo.tipo_veiculo:
                tipo_veiculo = noticia.cd_veiculo.tipo_veiculo.descricao_tipo_veiculo.strip()  
                # print(f"Tipo de veículo retornado do banco: {tipo_veiculo}")  

                # Adicionar o tipo de veículo ao dicionário caso não exista
                if tipo_veiculo not in noticias_por_tipo:
                    noticias_por_tipo[tipo_veiculo] = []

                noticias_por_tipo[tipo_veiculo].append(noticia)

        # Ordenar as categorias pelo nome
        noticias_por_tipo = dict(sorted(noticias_por_tipo.items()))

        context['cliente'] = cliente
        context['noticias_por_tipo'] = noticias_por_tipo
        return context



class CategoriaListView(ListView):
    model = Categoriapalavrachave
    template_name = 'categoria_list.html'
    context_object_name = 'categorias'
    paginate_by = 10  # Paginação para 10 categorias por página

# 🔷 Criar uma nova categoria


class CategoriaCreateView(CreateView):
    model = Categoriapalavrachave
    template_name = 'categoria_create.html'
    form_class = CategoriaPalavraChaveForm
    success_url = reverse_lazy('categoria_list')

# 🔷 Visualizar detalhes de uma categoria


class CategoriaDetailView(DetailView):
    model = Categoriapalavrachave
    template_name = 'categoria_detail.html'
    context_object_name = 'categoria'

# 🔷 Atualizar uma categoria existente


class CategoriaUpdateView(UpdateView):
    model = Categoriapalavrachave
    template_name = 'categoria_update.html'
    form_class = CategoriaPalavraChaveForm
    success_url = reverse_lazy('categoria_list')

# 🔷 Excluir uma categoria


class CategoriaDeleteView(DeleteView):
    model = Categoriapalavrachave
    template_name = 'categoria_delete.html'
    success_url = reverse_lazy('categoria_list')

# 🔷 Listar palavras-chave de um cliente específico


class PalavraChaveListView(ListView):
    model = Palavrachave
    template_name = 'palavra_chave_list.html'
    context_object_name = 'palavras'
    paginate_by = 20  # Paginação para 20 palavras-chave por página

    def get_queryset(self):
        """
        Filtra as palavras-chave pelo cliente logado.
        """
        queryset = super().get_queryset()
        return queryset.filter(id_cliente=self.request.user.erpcliente)

# 🔷 Criar uma nova palavra-chave


class PalavraChaveCreateView(CreateView):
    model = Palavrachave
    template_name = 'palavra_chave_create.html'
    form_class = PalavraChaveForm
    success_url = reverse_lazy('palavra_chave_list')

# 🔷 Visualizar detalhes de uma palavra-chave


class PalavraChaveDetailView(DetailView):
    model = Palavrachave
    template_name = 'palavra_chave_detail.html'
    context_object_name = 'palavra'

# 🔷 Atualizar uma palavra-chave existente


class PalavraChaveUpdateView(UpdateView):
    model = Palavrachave
    template_name = 'palavra_chave_update.html'
    form_class = PalavraChaveForm

    def form_valid(self, form):
        """
        Salva o formulário e redireciona para a página de detalhes da palavra-chave.
        """
        self.object = form.save()
        return HttpResponseRedirect(reverse('palavra_chave_detail', kwargs={'pk': self.object.pk}))

# Excluir uma palavra-chave


class PalavraChaveDeleteView(DeleteView):
    model = Palavrachave
    template_name = 'palavra_chave_delete.html'
    success_url = reverse_lazy('palavra_chave_list')

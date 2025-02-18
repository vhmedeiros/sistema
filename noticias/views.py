from django.http import HttpResponseRedirect
from datetime import date
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from veiculos.models import Veiculosistemas, Uf, Municipio
from unidecode import unidecode
from django.db.models import Q
from django.db import connection
from django.contrib import messages
from .models import NoticiaImportada
from .forms import NoticiaImportadaForm


# class NoticiaListView(ListView):
#     model = NoticiaImportada
#     template_name = 'noticia_list.html'
#     context_object_name = 'noticias'
#     paginate_by = 20

#     def get_queryset(self):
#         queryset = super().get_queryset()
#         titulo = self.request.GET.get('titulo')
#         conteudo = self.request.GET.get('conteudo')
#         veiculo = self.request.GET.get('veiculo')
#         uf = self.request.GET.get('uf')
#         cidade = self.request.GET.get('cidade')

#         if titulo:
#             # Removendo acentos da busca
#             titulo_unaccented = unidecode(titulo)
#             queryset = queryset.filter(
#                 Q(titulo__icontains=titulo) |
#                 Q(titulo__icontains=titulo_unaccented)
#             )

#         if conteudo:
#             # Removendo acentos da busca
#             conteudo_unaccented = unidecode(conteudo)
#             queryset = queryset.filter(
#                 Q(conteudo__icontains=conteudo) |
#                 Q(conteudo__icontains=conteudo_unaccented)
#             )

#         if veiculo:
#             queryset = queryset.filter(cd_veiculo__id=veiculo)

#         if uf:
#             # Não é necessário remover acentos para uf, pois geralmente são siglas
#             queryset = queryset.filter(cd_veiculo__cd_uf__cd_uf=uf)

#         if cidade:
#             # Removendo acentos da busca
#             cidade_unaccented = unidecode(cidade)
#             queryset = queryset.filter(
#                 Q(cd_veiculo__id_municipio__nome_municipio__icontains=cidade) |
#                 Q(cd_veiculo__id_municipio__nome_municipio__icontains=cidade_unaccented)
#             )

#         return queryset

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['veiculos'] = Veiculosistemas.objects.all()
#         context['ufs'] = Uf.objects.values_list('cd_uf', flat=True).distinct()
#         uf_selecionada = self.request.GET.get('uf')

#         if uf_selecionada:
#             context['cidades'] = Municipio.objects.filter(
#                 uf_municipio=uf_selecionada
#             ).order_by('nome_municipio').values_list('id_municipio', 'nome_municipio')
#         else:
#             context['cidades'] = []

#         context['today'] = date.today()
#         return context

class NoticiaListView(ListView):
    model = NoticiaImportada
    template_name = 'noticia_list.html'
    context_object_name = 'noticias'
    paginate_by = 20

    def get_queryset(self):
        queryset = NoticiaImportada.objects.select_related('cd_veiculo').only(
            'titulo', 'conteudo', 'cd_veiculo__nome_veiculo', 'dt_noticia', 'dt_importacao'
        )  # 🔹 Carrega apenas os campos necessários

        titulo = self.request.GET.get('titulo')
        conteudo = self.request.GET.get('conteudo')
        veiculo = self.request.GET.get('veiculo')
        uf = self.request.GET.get('uf')
        cidade = self.request.GET.get('cidade')

        if titulo:
            queryset = queryset.filter(titulo__icontains=titulo)

        if conteudo:
            queryset = queryset.filter(conteudo__icontains=conteudo)

        if veiculo:
            queryset = queryset.filter(cd_veiculo_id=veiculo)

        if uf:
            queryset = queryset.filter(cd_veiculo__cd_uf=uf)

        if cidade:
            queryset = queryset.filter(cd_veiculo__id_municipio=cidade)

        return queryset.order_by('-dt_noticia')  # 🔹 Ordena de forma eficiente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # 🔹 Cacheando veículos para evitar repetidas consultas
        context['veiculos'] = list(Veiculosistemas.objects.values('cd_veiculo', 'nome_veiculo'))

        # 🔹 Cacheando UFs
        context['ufs'] = list(Uf.objects.values_list('cd_uf', flat=True).distinct())

        uf_selecionada = self.request.GET.get('uf')

        if uf_selecionada:
            context['cidades'] = list(Municipio.objects.filter(
                uf_municipio=uf_selecionada
            ).values_list('id_municipio', 'nome_municipio'))
        else:
            context['cidades'] = []

        context['today'] = date.today()
        return context

class NoticiaCreateView(CreateView):
    model = NoticiaImportada
    template_name = 'noticia_create.html'
    form_class = NoticiaImportadaForm
    success_url = reverse_lazy('noticia_list')

    def form_valid(self, form):
        # Salva o objeto manualmente
        self.object = form.save()

        try:
            with connection.cursor() as cursor:
                cursor.execute("EXEC VincularNoticiasAClientes;")
        except Exception as e:
            messages.error(self.request, f"Erro ao processar notícia: {e}")
            return HttpResponseRedirect(reverse('noticia_list'))

        return super().form_valid(form)


class NoticiaDetailView(DetailView):
    model = NoticiaImportada
    template_name = 'noticia_detail.html'
    context_object_name = 'noticias'

# class NoticiaUpdateView(UpdateView):
#     model = NoticiaImportada
#     template_name = 'noticia_update.html'
#     form_class = NoticiaImportadaForm
#     success_url = reverse_lazy('noticia_list')
#     # def get_success_url(self):
#     #     return reverse('noticia_detail', kwargs={'pk': self.object.pk})


class NoticiaUpdateView(UpdateView):
    model = NoticiaImportada
    template_name = 'noticia_update.html'
    form_class = NoticiaImportadaForm

    def form_valid(self, form):
        # Salva o objeto manualmente
        self.object = form.save()

        # Redireciona para a página de detalhes da notícia específica
        return HttpResponseRedirect(reverse('noticia_detail', kwargs={'pk': self.object.pk}))

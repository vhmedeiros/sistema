from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from . import models, forms


class ErpContratoListView(ListView):
    model = models.ErpContrato
    template_name = 'contrato_list.html'


class ErpContratoDetailView(DetailView):
    model = models.ErpContrato
    template_name = 'contrato_detail.html'


class ErpContratoCreateView(CreateView):
    model = models.ErpContrato
    form_class = forms.ErpContratoForm
    template_name = 'contrato_create.html'

    def form_valid(self, form):
        # obetem o ID do cliente a partir dos parametros da URL
        # a propriedade 'kwargs' armazena os parametros da URL
        # e o metodo 'get' retorna o valor do parametro 'cliente_id'
        cliente_id = self.kwargs.get('cliente_id')

        # obtem o objeto cliente a partir do ID, vindo do BD
        # ou retorna um erro 404 caso o objeto não exista
        cliente = get_object_or_404(models.ErpCliente, pk=cliente_id)

        # atribui o objeto cliente ao campo 'id_cliente' do formulario
        form.instance.id_cliente = cliente

        # chama o metodo 'form_valid' da classe pai
        return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        # obtem o formulario da classe pai
        form = super().get_form(*args, **kwargs)

        if 'id_cliente' in form.fields:
            form.fields.pop('id_cliente')
            
        return form

    def get_context_data(self, **kwargs):
        # adiciona o ID do cliente ao contexto do template
        context = super().get_context_data(**kwargs)
        context['cliente_id'] = self.kwargs.get('cliente_id')
        return context

    def get_success_url(self):
        # Redirecionar para a página de detalhes do contrato criado
        return reverse('contrato_detail', kwargs={'pk': self.object.pk})
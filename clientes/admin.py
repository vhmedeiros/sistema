from django.contrib import admin
from .models import Installsistemas, ErpCliente


@admin.register(Installsistemas)
class InstallsistemasAdmin(admin.ModelAdmin):
    # Campos exibidos na lista do admin
    list_display = (
        'cd_cliente_sistema', 'nome_cliente', 'nome_cliente_sistema', 'ativo_no_sistema',
        'diretorio_sistema', 'cd_modelo_pagina_cliente', 'cd_ordenacao',
        'tipo_arquivo_preferencial', 'nome_imagem_logo', 'cd_empresa', 'dt_ativacao'
    )

    # Filtros laterais
    list_filter = (
        'ativo_no_sistema', 'cd_modelo_pagina_cliente', 'cd_empresa', 'dt_ativacao',
        'in_bloqueio_site', 'in_avalia_noticia', 'in_email_bloqueado',
        'in_site_iis_ok', 'in_materia_dia_publicacao', 'in_apenas_veiculo_contratado',
        'in_apenas_categoria_principal', 'in_exibe_espaco_ocupado', 'in_exibe_valoracao',
        'in_exibe_avaliacao', 'in_obrigatorio_usuario_senha', 'in_exibe_logo_noticia',
        'in_incluir_vinheta'
    )

    # Campos que podem ser pesquisados
    search_fields = (
        'nome_cliente', 'nome_cliente_sistema', 'diretorio_sistema',
        'tipo_arquivo_preferencial', 'nome_imagem_logo', 'cd_ordenacao',
        'id_google_analytics', 'observacao', 'nome_grupo_veiculo_ordenado',
        'nome_grupo_veiculo_nao_ordenado', 'nome_grupo_veiculo_coluna'
    )

    # Campos que permitem ordenação
    ordering = ('-cd_cliente_sistema', 'nome_cliente', 'nome_cliente_sistema', 'dt_ativacao')

    # Campos exibidos como links clicáveis na lista
    list_display_links = ('cd_cliente_sistema', 'nome_cliente', 'nome_cliente_sistema')

    # Campos que podem ser editados diretamente na lista
    list_editable = ('ativo_no_sistema', 'cd_modelo_pagina_cliente', 'cd_empresa')

    # Adiciona paginação no admin
    list_per_page = 25


@admin.register(ErpCliente)
class ErpClienteAdmin(admin.ModelAdmin):
    # Campos que serão exibidos na lista do admin
    list_display = (
        'id_cliente',
        'nome_cliente',
        'numero_cnpj',
        'numero_cpf',
        'status_cliente',
        'data_cadastro',
    )
    # Campos que serão utilizados para busca
    search_fields = (
        'nome_cliente',
        'numero_cnpj',
        'numero_cpf',
        'nome_razao_social',
    )
    # Campos que podem ser filtrados
    list_filter = (
        'status_cliente',
        'cd_uf',
        'data_cadastro',
    )
    # Campos que podem ser editados diretamente na lista
    list_editable = ('status_cliente',)
    # Campos que organizam a visualização por data de cadastro
    date_hierarchy = 'data_cadastro'
    # Configuração para exibição em colunas no formulário de edição
    fieldsets = (
        ('Informações Básicas', {
            'fields': (
                'nome_cliente',
                'nome_razao_social',
                'numero_cnpj',
                'numero_cpf',
                'status_cliente',
                'data_cadastro',
            )
        }),
        ('Endereço', {
            'fields': (
                'logradouro',
                'complemento',
                'bairro',
                'numero_endereco',
                'cep',
                'cd_pais',
                'cd_uf',
                'id_municipio',
            )
        }),
        ('Contato', {
            'fields': (
                'telefone_gestor',
                'email_gestor',
                'contato_gestor',
                'telefone_financeiro',
                'email_financeiro',
                'contato_financeiro',
                'telefone_usuario',
                'email_usuario',
                'contato_usuario',
            )
        }),
        ('Informações Adicionais', {
            'fields': (
                'numero_inscricao_estadual',
                'numero_inscricao_municipal',
                'id_ultimo_servico_pago',
            )
        }),
    )


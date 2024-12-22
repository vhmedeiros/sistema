from django.db import models
from empresas.models import ErpEmpresa
from veiculos.models import Municipio, Uf


class ErpCliente(models.Model):
    id_cliente = models.AutoField(
        primary_key=True, verbose_name='ID do Cliente')
    numero_cnpj = models.CharField(db_column='nr_cnpj',
                                   max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True, verbose_name='CNPJ'
                                   )
    numero_cpf = models.CharField(db_column='nr_cpf',
                                  max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                  blank=True, null=True, verbose_name='CPF'
                                  )
    nome_cliente = models.CharField(db_column='no_cliente',
                                    max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                    verbose_name='Nome do Cliente'
                                    )
    nome_razao_social = models.CharField(db_column='no_razao_social',
                                         max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                         blank=True, null=True, verbose_name='Razão Social'
                                         )
    numero_inscricao_estadual = models.CharField(db_column='nr_insc_estadual',
                                                 max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                                 blank=True, null=True, verbose_name='Inscrição Estadual'
                                                 )
    endereco = models.CharField(db_column='no_endereco',
                                max_length=600, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                blank=True, null=True, verbose_name='Endereço'
                                )
    telefone_gestor = models.CharField(db_column='nr_telefone_gestor',
                                       max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                       blank=True, null=True, verbose_name='Telefone do Gestor'
                                       )
    email_gestor = models.CharField(db_column='no_email_gestor',
                                    max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                    blank=True, null=True, verbose_name='E-mail do Gestor'
                                    )
    contato_gestor = models.CharField(db_column='no_contato_gestor',
                                      max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                      blank=True, null=True, verbose_name='Contato do Gestor'
                                      )
    contato_financeiro = models.CharField(db_column='no_contato_financeiro',
                                          max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                          blank=True, null=True, verbose_name='Contato Financeiro'
                                          )
    telefone_financeiro = models.CharField(db_column='nr_telefone_financeiro',
                                           max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                           blank=True, null=True, verbose_name='Telefone Financeiro'
                                           )
    email_financeiro = models.CharField(db_column='no_email_financeiro',
                                        max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                        blank=True, null=True, verbose_name='E-mail Financeiro'
                                        )
    contato_usuario = models.CharField(db_column='no_contato_usuario',
                                       max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                       blank=True, null=True, verbose_name='Contato do Usuário'
                                       )
    telefone_usuario = models.CharField(db_column='nr_telefone_usuario',
                                        max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                        blank=True, null=True, verbose_name='Telefone do Usuário'
                                        )
    email_usuario = models.CharField(db_column='no_email_usuario',
                                     max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                     blank=True, null=True, verbose_name='E-mail do Usuário'
                                     )
    status_cliente = models.CharField(db_column='st_cliente',
                                      max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                      verbose_name='Status do Cliente'
                                      )
    data_cadastro = models.DateTimeField(
        db_column='dt_cadastro', verbose_name='Data de Cadastro')
    numero_inscricao_municipal = models.CharField(db_column='nr_insc_municipal',
                                                  max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                                  blank=True, null=True, verbose_name='Inscrição Municipal'
                                                  )
    logradouro = models.CharField(db_column='no_logradouro',
                                  max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                  blank=True, null=True, verbose_name='Logradouro'
                                  )
    complemento = models.CharField(db_column='no_complemento',
                                   max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                   blank=True, null=True, verbose_name='Complemento'
                                   )
    bairro = models.CharField(db_column='no_bairro',
                              max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS',
                              blank=True, null=True, verbose_name='Bairro'
                              )
    numero_endereco = models.CharField(db_column='nr_endereco',
                                       max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
                                       blank=True, null=True, verbose_name='Número'
                                       )
    cep = models.CharField(db_column='nr_cep',
                           max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS',
                           blank=True, null=True, verbose_name='CEP'
                           )
    cd_pais = models.CharField(
        max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', 
        blank=True, null=True, verbose_name='Código do País'
    )
    cd_uf = models.ForeignKey(Uf, on_delete=models.DO_NOTHING, db_column='sg_uf',
                              max_length=2,  # FK
                              blank=True, null=True, verbose_name='UF'
                              )
    id_municipio = models.ForeignKey(Municipio, models.DO_NOTHING, db_column='id_municipio',
                                     blank=True, null=True, verbose_name='Município' 
                                     )
    id_ultimo_servico_pago = models.IntegerField(
        blank=True, null=True, verbose_name='ID do Último Serviço Pago'
    )

    class Meta:
        managed = False
        db_table = 'erp_cliente'
        verbose_name = 'ERP Cliente'
        verbose_name_plural = 'ERP Clientes'
        ordering = ['id_cliente']

    def __str__(self):
        return self.nome_cliente


class Installsistemas(models.Model):
    cd_cliente_sistema = models.IntegerField(
        db_column='CodSys', primary_key=True, verbose_name='Código do Sistema'
    )
    nome_cliente = models.CharField(
        db_column='no_cliente',
        max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Nome do Cliente'
    )
    nome_cliente_sistema = models.CharField(
        db_column='NmoSys', max_length=100,
        db_collation='SQL_Latin1_General_CP1_CI_AS',
        verbose_name='Nome do Sistema'
    )
    ativo_no_sistema = models.BooleanField(
        db_column='ativosys', verbose_name='Ativo no Sistema'
    )
    diretorio_sistema = models.CharField(
        db_column='diretoriosys',
        max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS',
        verbose_name='Diretório do Sistema'
    )
    cd_modelo_pagina_cliente = models.CharField(
        db_column='cd_modelo',
        max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Modelo da Página do Cliente'
    )
    cd_ordenacao = models.CharField(
        max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Ordenação'
    )
    tipo_arquivo_preferencial = models.CharField(
        db_column='tp_arquivo_preferencial',
        max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Tipo de Arquivo Preferencial'
    )
    nome_imagem_logo = models.CharField(
        db_column='no_imagem_logo',
        max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Imagem do Logo'
    )
    cd_senha = models.CharField(
        max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Código da Senha'
    )
    in_bloqueio_site = models.CharField(
        max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Bloqueio no Site'
    )
    in_avalia_noticia = models.CharField(
        max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Avaliação da Notícia'
    )
    nome_cliente_pagina_sistema = models.CharField(
        db_column='PalavrasSys', max_length=500,
        db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True,
        verbose_name='Nome da Página do Cliente no Sistema'
    )
    nome_grupo_veiculo_ordenado = models.CharField(
        db_column='no_grupo_veiculo_ordenado',
        max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Grupo de Veículos Ordenados'
    )
    nome_grupo_veiculo_nao_ordenado = models.CharField(
        db_column='no_grupo_veiculo_nao_ordenado',
        max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Grupo de Veículos Não Ordenados'
    )
    nome_grupo_veiculo_coluna = models.CharField(
        db_column='no_grupo_veiculo_coluna',
        max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Grupo de Veículos em Coluna'
    )
    in_email_bloqueado = models.CharField(
        max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Email Bloqueado'
    )
    id_google_analytics = models.CharField(
        max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='ID do Google Analytics'
    )
    observacao = models.CharField(
        db_column='tt_observacao',
        max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Observações'
    )
    in_site_iis_ok = models.CharField(
        max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Site IIS OK'
    )
    in_materia_dia_publicacao = models.CharField(
        max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Matéria no Dia de Publicação'
    )
    in_apenas_veiculo_contratado = models.CharField(
        max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Apenas Veículo Contratado'
    )
    id_cliente = models.ForeignKey(
        ErpCliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True
    )
    tp_sistema = models.CharField(
        max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Tipo de Sistema'
    )
    in_apenas_categoria_principal = models.CharField(
        max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Apenas Categoria Principal'
    )
    id_contrato = models.IntegerField(
        blank=True, null=True, verbose_name='ID do Contrato'  # FK
    )
    id_proposta = models.IntegerField(
        blank=True, null=True, verbose_name='ID da Proposta'  # FK
    )
    in_exibe_espaco_ocupado = models.CharField(
        max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Exibe Espaço Ocupado'
    )
    in_exibe_valoracao = models.CharField(
        max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Exibe Valoração'
    )
    in_exibe_avaliacao = models.CharField(
        max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Exibe Avaliação'
    )
    cd_empresa = models.ForeignKey(
        ErpEmpresa, models.DO_NOTHING, db_column='cd_empresa'
    )

    dt_ativacao = models.DateTimeField(
        blank=True, null=True, verbose_name='Data de Ativação'
    )
    in_obrigatorio_usuario_senha = models.CharField(
        max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Usuário e Senha Obrigatórios'
    )
    in_exibe_logo_noticia = models.CharField(
        max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS',
        blank=True, null=True, verbose_name='Exibe Logo na Notícia'
    )
    in_incluir_vinheta = models.CharField(
        db_column='In_incluir_vinheta', max_length=1,
        db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True,
        verbose_name='Incluir Vinheta'
    )

    class Meta:
        managed = False
        db_table = 'InstallSistemas'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome_cliente_sistema
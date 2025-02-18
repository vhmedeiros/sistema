# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from clientes.models import ErpCliente, ErpEmpresa
from noticias.models import NoticiaImportada


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
        verbose_name_plural = 'Configurações do Cliente'

        def __str__(self):
            return self.no_cliente


class Categoriapalavrachave(models.Model):
    nome = models.CharField(unique=True, max_length=255,
                            db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'CategoriaPalavraChave'

    def __str__(self):
        return self.nome


class Palavrachave(models.Model):
    id_cliente = models.ForeignKey(
        ErpCliente, models.DO_NOTHING, db_column='id_cliente')
    id_categoria = models.ForeignKey(
        Categoriapalavrachave, models.DO_NOTHING, db_column='id_categoria')
    palavra = models.CharField(
        max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    data_cadastro = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'PalavraChave'
        unique_together = (('id_cliente', 'palavra'),)

    def __str__(self):
        return self.palavra

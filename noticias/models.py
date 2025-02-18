from django.db import models
from veiculos.models import Veiculosistemas

class NoticiaImportada(models.Model):
    cd_noticia = models.AutoField(primary_key=True)
    id_importacao = models.IntegerField(null=True, blank=True)
    dt_importacao = models.DateTimeField()
    dt_noticia = models.DateTimeField()
    titulo = models.CharField(db_column='no_titulo',
        max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    conteudo = models.CharField(max_length=4000, db_column='tt_noticia', db_collation='SQL_Latin1_General_CP1_CI_AS')
    cd_veiculo = models.ForeignKey(
        Veiculosistemas, models.DO_NOTHING, db_column='id_veiculo')
    ds_url = models.CharField(
        max_length=500, db_collation='SQL_Latin1_General_CP1_CI_AS')
    subtitulo = models.CharField(db_column='tt_sutia',
        max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_editoria = models.IntegerField(blank=True, null=True)
    no_colunista = models.CharField(
        max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    ds_url_media = models.CharField(
        max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    cd_pagina = models.CharField(
        max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    clientes_relacionados = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    categorias_relacionadas = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    processado = models.BooleanField(blank=True, null=True, default=False)

    class Meta:
        managed = False
        db_table = 'noticia_importada'
        verbose_name_plural = 'Notícias Importadas'
        ordering = ['-dt_noticia']

    def __str__(self):
        return self.titulo

    
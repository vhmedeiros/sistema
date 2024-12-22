from django.db import models
from empresas.models import ErpEmpresa
from clientes.models import ErpCliente

TIPO_COBRANCA = (
    ['MES', 'Mensal'],
    ['ANO', 'Anual'],
    ['OUT', 'Outro'],
)

ENVIO_NOTA_FISCAL = (
    ['A', 'Email Automático'],
    ['M', 'Email Manual'],
    ['C', 'Correios'],
    ['O', 'Outro'],
)


class ErpContrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(ErpCliente, models.DO_NOTHING, db_column='id_cliente')
    cd_empresa = models.ForeignKey(ErpEmpresa, models.DO_NOTHING, db_column='cd_empresa')
    cd_identificacao = models.CharField(max_length=20, db_collation='SQL_Latin1_General_CP850_CI_AI', blank=True, null=True)
    descricao_contrato = models.CharField(max_length=1000, db_collation='SQL_Latin1_General_CP850_CI_AI')
    data_inicio_vigencia = models.DateField()
    data_fim_vigencia = models.DateField()
    tipo_prorrogacao = models.CharField(max_length=3, db_collation='SQL_Latin1_General_CP850_CI_AI')
    descricao_objeto = models.TextField(db_collation='SQL_Latin1_General_CP850_CI_AI')
    informacao_adicional = models.TextField(db_collation='SQL_Latin1_General_CP850_CI_AI', blank=True, null=True)
    valor_contrato = models.DecimalField(max_digits=19, decimal_places=4)
    dia_emissao_nota_fiscal = models.IntegerField()
    status_contrato = models.CharField(max_length=1, db_collation='SQL_Latin1_General_CP850_CI_AI')
    in_contrato_assinado = models.BooleanField()
    tipo_cobranca = models.CharField(max_length=3, db_collation='SQL_Latin1_General_CP850_CI_AI')
    data_cadastro = models.DateTimeField()
    dia_do_pagamento = models.IntegerField()
    dia_aviso_fim_vigencia = models.IntegerField(blank=True, null=True)
    forma_envio_nf = models.CharField(max_length=1, db_collation='SQL_Latin1_General_CP850_CI_AI', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'erp_contrato'
        ordering = ['cd_empresa', 'id_cliente', 'id_contrato']
        verbose_name = 'Contrato'

    def __str__(self):
        return str(self.id_contrato)
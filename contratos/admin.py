from django.contrib import admin
from .models import ErpContrato


@admin.register(ErpContrato)
class ErpContratoAdmin(admin.ModelAdmin):
    list_display = ('id_contrato', 'id_cliente', 'cd_empresa', 'descricao_contrato', 'data_inicio_vigencia', 'data_fim_vigencia', 'tipo_prorrogacao',
                    'descricao_objeto', 'informacao_adicional', 'valor_contrato', 'dia_emissao_nota_fiscal', 'status_contrato',
                    'in_contrato_assinado', 'tipo_cobranca', 'data_cadastro', 'dia_do_pagamento', 'dia_aviso_fim_vigencia', 'forma_envio_nf')
    search_fields = ('id_contrato', 'id_cliente', 'cd_empresa', 'descricao_contrato', 'data_inicio_vigencia', 'data_fim_vigencia',
                     'tipo_prorrogacao', 'descricao_objeto', 'informacao_adicional', 'valor_contrato', 'dia_emissao_nota_fiscal', 'status_contrato',)
    list_per_page = 50

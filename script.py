# -*-* coding: utf-8 -*-
from contratos.models import ErpProduto

# Lista de produtos e sua hierarquia completa
produtos = [
    {"descricao": "CLIPPING", "produto_principal": None},
    {"descricao": "CLIPPING / IMPRESSO", "produto_principal": "CLIPPING"},
    {"descricao": "CLIPPING / IMPRESSO / NACIONAL",
        "produto_principal": "CLIPPING / IMPRESSO"},
    {"descricao": "CLIPPING / IMPRESSO / NACIONAL / CLIPAGEM",
        "produto_principal": "CLIPPING / IMPRESSO / NACIONAL"},
    {"descricao": "CLIPPING / IMPRESSO / NACIONAL / IMAGEM A4",
        "produto_principal": "CLIPPING / IMPRESSO / NACIONAL"},
    {"descricao": "CLIPPING / IMPRESSO / NACIONAL / PÁGINA INTEIRA",
        "produto_principal": "CLIPPING / IMPRESSO / NACIONAL"},
    {"descricao": "CLIPPING / IMPRESSO / REGIONAL",
        "produto_principal": "CLIPPING / IMPRESSO"},
    {"descricao": "CLIPPING / IMPRESSO / REGIONAL / IMAGEM A4",
        "produto_principal": "CLIPPING / IMPRESSO / REGIONAL"},
    {"descricao": "CLIPPING / IMPRESSO / REGIONAL / PÁGINA INTEIRA",
        "produto_principal": "CLIPPING / IMPRESSO / REGIONAL"},
]

# Adicionar UFs para CLIPPING / IMPRESSO / REGIONAL
ufs = ["AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", "MG", "MS", "MT",
       "PA", "PB", "PE", "PI", "PR", "RJ", "RN", "RO", "RR", "RS", "SC", "SE", "SP", "TO"]
for uf in ufs:
    produtos.append({"descricao": f"CLIPPING / IMPRESSO / REGIONAL / UF: {uf}",
                    "produto_principal": "CLIPPING / IMPRESSO / REGIONAL"})

produtos.extend([
    {"descricao": "CLIPPING / RÁDIO", "produto_principal": "CLIPPING"},
    {"descricao": "CLIPPING / RÁDIO / NACIONAL",
        "produto_principal": "CLIPPING / RÁDIO"},
    {"descricao": "CLIPPING / RÁDIO / REGIONAL",
        "produto_principal": "CLIPPING / RÁDIO"},
])

# Adicionar UFs para CLIPPING / RÁDIO / REGIONAL
for uf in ufs:
    produtos.append({"descricao": f"CLIPPING / RÁDIO / REGIONAL / UF: {uf}",
                    "produto_principal": "CLIPPING / RÁDIO / REGIONAL"})

produtos.extend([
    {"descricao": "CLIPPING / REDES SOCIAIS", "produto_principal": "CLIPPING"},
    {"descricao": "CLIPPING / REVISTA", "produto_principal": "CLIPPING"},
    {"descricao": "CLIPPING / REVISTA / ESPECIALIZADAS",
        "produto_principal": "CLIPPING / REVISTA"},
    {"descricao": "CLIPPING / REVISTA / NACIONAL",
        "produto_principal": "CLIPPING / REVISTA"},
    {"descricao": "CLIPPING / REVISTA / REGIONAL",
        "produto_principal": "CLIPPING / REVISTA"},
])

# Adicionar UFs para CLIPPING / REVISTA / REGIONAL
for uf in ufs:
    produtos.append({"descricao": f"CLIPPING / REVISTA / REGIONAL / UF: {uf}",
                    "produto_principal": "CLIPPING / REVISTA / REGIONAL"})

produtos.extend([
    {"descricao": "CLIPPING / TV", "produto_principal": "CLIPPING"},
    {"descricao": "CLIPPING / TV / NACIONAL",
        "produto_principal": "CLIPPING / TV"},
    {"descricao": "CLIPPING / TV / REGIONAL",
        "produto_principal": "CLIPPING / TV"},
])

# Adicionar UFs para CLIPPING / TV / REGIONAL
for uf in ufs:
    produtos.append({"descricao": f"CLIPPING / TV / REGIONAL / UF: {uf}",
                    "produto_principal": "CLIPPING / TV / REGIONAL"})

produtos.extend([
    {"descricao": "CLIPPING / WEB", "produto_principal": "CLIPPING"},
    {"descricao": "CLIPPING / WEB / NACIONAL",
        "produto_principal": "CLIPPING / WEB"},
    {"descricao": "CLIPPING / WEB / NACIONAL / FAC-SIMILE|PRINT SCREEN",
        "produto_principal": "CLIPPING / WEB / NACIONAL"},
    {"descricao": "CLIPPING / WEB / REGIONAL",
        "produto_principal": "CLIPPING / WEB"},
    {"descricao": "CLIPPING / WEB / REGIONAL / FAC-SIMILE|PRINT SCREEN",
        "produto_principal": "CLIPPING / WEB / REGIONAL"},
])

# Adicionar UFs para CLIPPING / WEB / REGIONAL
for uf in ufs:
    produtos.append({"descricao": f"CLIPPING / WEB / REGIONAL / UF: {uf}",
                    "produto_principal": "CLIPPING / WEB / REGIONAL"})

# Inserir produtos no banco de dados
for produto in produtos:
    # Buscar o produto principal, se existir
    principal = ErpProduto.objects.filter(descricao=produto["produto_principal"]).first(
    ) if produto["produto_principal"] else None

    # Criar o produto
    ErpProduto.objects.create(
        descricao=produto["descricao"],
        cd_produto_principal=principal,
        situacao_produto=True
    )

print("Todos os produtos foram adicionados com sucesso!")

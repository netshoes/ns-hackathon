from google.cloud import bigquery
from .utils import parse_date

client = bigquery.Client()

def buscar_pedido_por_id(id_pedido):
    _query = (
        f"select * from `dadosBrutos.orders` where HKT_CODIGO_PEDIDO = '{id_pedido}'"
    )
    results = list(client.query(_query).result())
    return len(results) > 0 and results[0] or None

def buscar_pedido_mais_recente_por_nome(id_usuario, nome):
    _query = (
        f"select o.HKT_ID_USUARIO, o.HKT_CODIGO_PEDIDO, p.DES_PROD, o.HKT_DATA_PEDIDO from `dadosBrutos.orders` as o "
        f"join `dadosBrutos.skusPrecoLog1P` as p on o.HKT_SKU_FILHO = p.COD_SKU_FILHO "
        f"where HKT_ID_USUARIO = '{id_usuario}' and lower(p.DES_PROD) like '%{nome}%'"
    )
    results = list(client.query(_query).result())
    results_by_date = sorted(results, key=(lambda r: parse_date(r.get("HKT_DATA_PEDIDO"))), reverse=True)
    return len(results_by_date) > 0 and results[0] or None

TABELA_TELEFONES_USUARIOS = {
    "5511999475937": "3158017899"
}

def buscar_usuario_por_tel(tel):
    tel = str(tel)
    if tel not in TABELA_TELEFONES_USUARIOS:
        return None
    return int(TABELA_TELEFONES_USUARIOS[tel])

# hehe xd
TABELA_TELEFONES_PEDIDOS = {
    "698762610": "722233605"
}

def buscar_cod_pedido_por_tel(tel):
    tel = str(tel)
    if tel not in TABELA_TELEFONES_PEDIDOS:
        return None
    return int(TABELA_TELEFONES_PEDIDOS[tel])

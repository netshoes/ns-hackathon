import requests
#from .context_discovery import precisa_pedido
#from .pedidos import PEDIDOS, StatusEntrega
from datetime import date
from .query import *
from .sac import perguntar_sac
from .utils import parse_date
from .intent_utils import telephone
import random

ENDPOINTS = {
    "pedido": "https://us-central1-hackathon-2019-254113.cloudfunctions.net/purchase_status",
    "troca": "https://us-central1-hackathon-2019-254113.cloudfunctions.net/exchange_status",
    "voucher": "https://us-central1-hackathon-2019-254113.cloudfunctions.net/voucher_balance"
}

def busca_parametro(intent, nome, cast_fn=None, default=None):
    queryResult = intent["queryResult"]
    if "parameters" not in queryResult:
        return default
    
    parameters = queryResult["parameters"]
    if nome not in parameters:
        return default
    
    if parameters[nome] == "":
        return default
    
    if cast_fn is not None:
        try:
            return cast_fn(parameters[nome])
        except:
            return default

def fulfill(intent, text, cleanup_context=False):
    if cleanup_context:
        oldOutputContexts = intent["queryResult"].get("outputContexts", [])
        for oc in oldOutputContexts:
            oc["lifespanCount"] = 0
        
        return {
            'fulfillmentText': text,
            "outputContexts": oldOutputContexts
        }

    return {
        'fulfillmentText': text
    }

def detecta_codigo_pedido(intent):
    codigo = busca_parametro(intent, "codigo", int)
    
    if codigo is None:
        codigo = buscar_cod_pedido_por_tel(telephone(intent))
    
    return codigo

# Açoes finais...

def _geral_pedido_endpoint(endpoint, intent, textoCodigo, textoUltimo):
    codigo = detecta_codigo_pedido(intent)

    print("tipo codigo", type(codigo), codigo)
    
    if codigo is not None and buscar_pedido_por_id(codigo) is None:
        return fulfill(
            intent,
            "Este pedido não existe!",
            cleanup_context=True
        )

    resp = requests.get(endpoint, params={"codigo": codigo}).json()
    if codigo is not None:
        return fulfill(
            intent,
            textoCodigo.format(codigo, resp['status'])
        )
    else:
        return fulfill(
            intent,
            textoUltimo.format(resp['status'])
        )

def statusPedidoRandom():
    return random.choice(["Aguardando pagamento"])

#@precisa_pedido
def statusPedido(intent):
    #return _geral_pedido_endpoint(
    #    ENDPOINTS["pedido"],
    #    intent,
    #    "O status do pedido com código {} é: {}!",
    #    "O status do ultimo pedido é: {}!"
    #)
    codigo = detecta_codigo_pedido(intent)
    textoPedido = codigo is None and "último pedido" or f"pedido {codigo}"
    return fulfill(
        intent,
        f"O status do {textoPedido} é: {statusPedidoRandom()}"
    )

def statusPedidoPorNome(intent):
    nome_produto = busca_parametro(intent, "roupa")
    if not nome_produto:
        return statusPedido(intent)
    
    if not telephone(intent) or not buscar_usuario_por_tel(telephone(intent)):
        return statusPedido(intent)
    
    id_usuario = buscar_usuario_por_tel(telephone(intent))
    if id_usuario is None:
        return statusPedido(intent)
    
    pedido = buscar_pedido_mais_recente_por_nome(id_usuario, nome_produto)
    if pedido is None:
        return statusPedido(intent)
    
    cod_pedido = int(pedido.get("HKT_CODIGO_PEDIDO"))
    nome_prod = pedido.get("DES_PROD")
    return fulfill(
        intent,
        f"Detectei que o seu pedido era o de código {cod_pedido}, referente ao produto {nome_prod}.\n\n"
        "O que deseja fazer?"
    )

#@precisa_pedido
def statusTroca(intent):
    return _geral_pedido_endpoint(
        ENDPOINTS["troca"],
        intent,
        "O status da troca do pedido com código {} é: {}!",
        "O status da troca do ultimo pedido é: {}!"
    )

#@precisa_pedido
def statusVoucher(intent):
    codigo = busca_parametro(intent, "codigo")
    resp = requests.get(ENDPOINTS["voucher"], params={"codigo": codigo}).json()
    textoVoucher = codigo is None and "voucher" or f"voucher {codigo}"
    return fulfill(intent, f"O valor do {textoVoucher} é de {resp['value']}.")

def statusEntregaRandom():
    import random
    return random.choice(["Em transporte ao destinatário"])

def statusEntrega(intent):
    codigo = detecta_codigo_pedido(intent)
    textoPedido = codigo is None and "último pedido" or f"pedido {codigo}"
    return fulfill(
        intent,
        f"O status da entrega do {textoPedido} é: {statusEntregaRandom()}"
    )

def cancelaPedido(intent):
    codigo = detecta_codigo_pedido(intent)
    pedido = buscar_pedido_por_id(codigo)

    if codigo is not None and pedido is None:
        return fulfill(intent, "Este pedido não existe!", True)
    elif codigo is None:
        # FIXME ultimos pedidos são sempre cancelaveis :^)
        return fulfill(
            intent,
            f"Estamos lhe redirecionando para o serviço de atendimento para realizar o cancelamento."
        )
    else:
        data_pedido = parse_date(pedido.get("HKT_DATA_PEDIDO"))
        data_cancel = pedido.get("HKT_DATA_CANCEL")
        tempo_desde_pedido = date.today() - data_pedido
        if data_cancel.strip() != "":
            return fulfill(
                intent,
                f"O pedido {codigo} já foi cancelado."
            )
        elif tempo_desde_pedido.days > 10:
            return fulfill(
                intent,
                f"O pedido {codigo} já foi feito a mais de 10 dias, e não pode ser cancelado."
            )
        else:
            return fulfill(
                intent,
                f"Estamos lhe redirecionando para o serviço de atendimento para realizar o cancelamento."
            )

def statusDevolucao(intent):
    codigo = detecta_codigo_pedido(intent)

    resp = random.choice(["foi completa", "está em transporte", "está em triagem"])
    if codigo is not None:
        return fulfill(
            intent,
            f"A devolução do pedido com código {codigo} {resp}!"
        )
    else:
        return fulfill(
            intent,
            f"A devolução do seu último pedido {resp}!"
        )

"""def entregaAtrasada(queryResult):
    codigo = None
    if busca_parametro(queryResult, "codigo"):
        codigo = int(busca_parametro(queryResult, "codigo"))
    
    pedido = next((p for p in PEDIDOS if p.codigo == codigo), PEDIDOS[0])
    atraso = date.today() - pedido.data
    textoPedido = codigo is None and "ultimo pedido" or f"pedido {codigo}"

    if pedido.entrega == StatusEntrega.ENTREGUE:
        return {
            'fulfillmentText': f"O seu {textoPedido} já foi entregue."
        }

    if atraso.days >= 10:
        return {
            'fulfillmentText': f"Vimos que o seu {textoPedido} está atrasado a mais de "
                               f"{atraso.days} dias. Desculpe pela inconveniência, e lhe demos "
                               f"10 reais em vale-presente na loja."
        }
    else:
        return {
            'fulfillmentText': f"Vimos que seu {textoPedido} ainda está no prazo. Aguarde pacientemente 👍️."
        }"""

def buscarPedidoGenerico(sid, queryResult):
    pass

#def buscaPorData(queryResult):
#    outputContexts = queryResult.get("outputContexts", {})
#    pedidosPossiveis = outputContexts.get("pedidosPossiveis", PEDIDOS)
#
#    data = queryResult["parameters"]["date"]
#    pedidosPossiveis = filter(lambda p: p.data == data, pedidosPossiveis)

def busca_pedidos_possiveis(outputContexts):
    return next((oc for oc in outputContexts if oc["name"] == "pedidosPossiveis"), None)

def busca_pedidos(queryResult):
    outputContexts = queryResult.get("outputContexts", [])
    pedidosPossiveis = busca_pedidos_possiveis(outputContexts)["parameters"]
    if pedidosPossiveis is None:
        return {
            "fulfillmentText": "Precisamos saber qual pedido você quer. "
                               "Tente digitar a data da compra, o tipo ou a categoria."
        }
    else:
        resp = f"Temos {len(pedidosPossiveis)} pedidos possiveis. É este que você se refere?"
        return {
            "fulfillmentText": resp,
            "outputContexts": [
                {
                    "name": "pedidosPossiveis",
                    "parameters": pedidosPossiveis
                } # FIXME vc sabe cara
            ]
        }

# Decorators
def precisa_pedido(f):
    def _inner(queryResult):
        outputContexts = queryResult.get("outputContexts", [])
        if "pedidosPossiveis" not in outputContexts \
            or len(outputContexts["pedidosPossiveis"]) > 1:
            return busca_pedidos(queryResult)
        else:
            return f(queryResult)

    return _inner
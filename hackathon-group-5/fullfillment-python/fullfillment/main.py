from flask import Flask, request, make_response, jsonify, abort
import requests
from .actions import *
import os

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! veja /webhook"

actionsMap = {
    "statusPedido": statusPedido,
    "statusTroca": statusTroca,
    "statusVoucher": statusVoucher,
    "statusEntrega": statusEntrega,
    "statusDevolucao": statusDevolucao,
    "cancelaPedido": cancelaPedido
#    "entregaAtrasada": entregaAtrasada
}

def session_id(session):
    return session.split("/")[4]

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    intent = None
    try:
        intent = request.get_json(force=True)
    except:
        return abort(400) # Bad request
    print("RECEBI")
    print(intent)

    try:
        # Chamar ações que estão registradas.
        if intent["queryResult"]["action"] in actionsMap:
            action = actionsMap[intent["queryResult"]["action"]]
            mandar = action(intent)
            print("MANDAR")
            print(mandar)
            return make_response(jsonify(mandar))
    except Exception as e:
        print(e)
    
    # Talvez seja bom dar uma mensagem para o usuario decente
    return abort(404)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
from google.cloud import pubsub_v1
import time
from .dlflow import predict
import os
import json
import requests

project_id = "hackathon-2019-254113"
subscription_name = "hackathon05"

TELEFONES_PERMITIDOS = [
    "5511963987403",
    "5511988603846",
    "5511999475937"
]

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials_pubsub.json"
subscriber = pubsub_v1.SubscriberClient()
# The `subscription_path` method creates a fully qualified identifier
# in the form `projects/{project_id}/subscriptions/{subscription_name}`
subscription_path = subscriber.subscription_path(
    project_id, subscription_name)

_endpoint_envio = "https://us-central1-hackathon-2019-254113.cloudfunctions.net/message"
def enviar_msg(wa_id, msg):
    print(requests.post(_endpoint_envio, json={"message": msg, "phone": f"+{wa_id}"}).text)

def callback(message):
    print('Received message: {}'.format(message))
    try:
        # FIXME RESPONDER SO DE 1 NUMERO PRA N VIRAR VARZEA
        data = json.loads(message.data)
        print(data)
        print(data["contacts"])
        print(data["contacts"][0])
        wa_id = data["contacts"][0]["wa_id"]
        
        if wa_id not in TELEFONES_PERMITIDOS:
            message.ack()
            return
        
        msg = data["messages"][0]["text"]["body"]

        resposta = predict(wa_id, msg)
        print(resposta)
        
        enviar_msg(wa_id, resposta)
    except Exception as e:
        print("Exception", e)
    message.ack()

subscriber.subscribe(subscription_path, callback=callback)

# The subscriber is non-blocking. We must keep the main thread from
# exiting to allow it to process messages asynchronously in the background.
print('Listening for messages on {}'.format(subscription_path))
while True:
    time.sleep(60)
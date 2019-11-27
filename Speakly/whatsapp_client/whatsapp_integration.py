import dialogflow_v2 as dialogflow
import requests
from google.cloud import pubsub_v1
import json
from google.auth import jwt

import settings


session_client = dialogflow.SessionsClient()

def detect_intent_texts(project_id, session_id, text, language_code='pt-br'):
    """Returns the result of detect intent with texts as inputs.

    Using the same `session_id` between requests allows continuation
    of the conversation."""
    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    text_input = dialogflow.types.TextInput(
            text=text, language_code=language_code)

    query_input = dialogflow.types.QueryInput(text=text_input)

    response = session_client.detect_intent(
            session=session, query_input=query_input)

    print(response)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
            response.query_result.intent.display_name,
            response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
            response.query_result.fulfillment_text))
    return response

def send_whatsapp_message(phone_number, msg):
    r = requests.post(settings.WAPP_SEND_URL, json={
        "message": msg,
        "phone": phone_number
    })
    status = r.status_code
    print(f'msg to {phone_number} done with status {status}')

service_account_info = json.load(open("/home/rainsong/gcp/hack_whatsapp.json"))
audience = "https://pubsub.googleapis.com/google.pubsub.v1.Subscriber"

credentials = jwt.Credentials.from_service_account_info(
    service_account_info, audience=audience
)

subscriber = pubsub_v1.SubscriberClient(credentials=credentials)

topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id=settings.PROJECT_ID,
    topic=settings.TOPIC_NAME,
)
subscription_name = 'projects/{project_id}/subscriptions/{sub}'.format(
    project_id=settings.PROJECT_ID,
    sub=settings.SUB_NAME  # Set this to something appropriate.
)

# subscriber.create_subscription(
    # name=subscription_name, topic=topic_name)

def callback(req):
    data = json.loads(req.data.decode())
    message = data['messages'][0]
    print(message)
    req.ack()
    if message['from'] not in ['5511985730876', '5511968458580', '5511967171470', '5511983718789']:
        return
    print('=' * 20)

    df_response = detect_intent_texts('speakly-idmccc', message['from'], message['text']['body'])
    if df_response.query_result.fulfillment_text == '':
        df_response.query_result.fulfillment_text = 'Desculpe, não entendi'
    send_whatsapp_message(message['from'][2:], df_response.query_result.fulfillment_text)

future = subscriber.subscribe(subscription_name, callback)

def main():
    while True:
        try:
            print(future.result())
        except KeyboardInterrupt:
            future.cancel()
            return
        except:
            pass

# send_whatsapp_message('11985730876', 'Eae mano')
# detect_intent_texts('speakly-idmccc', '42', 'alow galera de cowboy')

main()

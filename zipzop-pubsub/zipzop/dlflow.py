import dialogflow_v2 as dialogflow
from google.protobuf.struct_pb2 import Struct, Value
import os

_project_id = "hackathon-05"

#client = dialogflow.SessionsClient(credentials={
#    "private_key": _private_key,
#    "client_email": _client_email
#})

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials_dialogflow.json"
client = dialogflow.SessionsClient()

def predict(session_id, message):
    session = client.session_path(_project_id, session_id)

    text_input = dialogflow.types.TextInput(
        text=message, language_code="pt-BR")

    query_input = dialogflow.types.QueryInput(text=text_input)
    struct = Struct(fields={"source": Value(string_value="whatsapp"), "wa_id": Value(string_value=session_id)})
    query_params = dialogflow.types.QueryParameters(payload=struct)
    response = client.detect_intent(
        session=session,
        query_input=query_input, 
        query_params=query_params
    )

    return response.query_result.fulfillment_text

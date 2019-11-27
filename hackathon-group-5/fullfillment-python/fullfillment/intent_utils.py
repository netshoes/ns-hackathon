def telephone(intent):
    originalIntent = intent["originalDetectIntentRequest"]

    if "source" in originalIntent and originalIntent["source"] == "telegram":
        return int(originalIntent["payload"]["from"]["id"])
    elif "payload" in originalIntent and "source" in originalIntent["payload"] and \
        originalIntent["payload"]["source"] == "whatsapp":
        return int(originalIntent["payload"]["wa_id"])

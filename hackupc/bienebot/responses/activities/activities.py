import json
import random


def get_message(response_type):
    """
    Return a message from a activities intent
    :param response_type luis response
    """
    with open('hackupc/bienebot/responses/activities/activities_data.json') as json_data:
        doc = json.load(json_data)
        return random.choice(doc['answer'])

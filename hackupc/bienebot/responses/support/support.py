import json
import random


def get_message(response_type):
    """
    Return a message from a support intent
    :param response_type luis response
    """
    with open('hackupc/bienebot/responses/support/support_data.json') as json_data:
        doc = json.load(json_data)
        return random.choice(doc['answer'])

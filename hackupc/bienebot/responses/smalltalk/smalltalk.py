import json
from random import randint


def get_message(response_type):
    """
    Return a message from a smalltalk intent
    :param response_type luis response
    """
    with open('hackupc/bienebot/responses/smalltalk/smalltalk_data.json') as json_data:
        doc = json.load(json_data)
        data = json.load(f)

        intent = response_type['topScoringIntent']['intent']
        entities = response_type['entities']
        list_intent = intent.split('.')

        length = data[intent[1]].length
        nrandom = randint(0,length-1)
        return data[intent[1]][nrandom]

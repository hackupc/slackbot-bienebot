import json
from random import randint
from hackupc.bienebot.util import log


def get_message(response_type):
    """
    Return a message from a smalltalk intent
    :param response_type luis response
    """


    with open('hackupc/bienebot/responses/smalltalk/smalltalk_data.json') as json_data:
        data = json.load(json_data)

        intent = response_type['topScoringIntent']['intent']
        #entities = response_type['entities']
        list_intent = intent.split('.')

        log.info('|RESPONSES| Looking for ['+ list_intent[1] + '] from JSON element')

        length = len(data[list_intent[1]])
        nrandom = randint(0,length-1)
        return data[list_intent[1]][nrandom]

import json
import random

from hackupc.bienebot.util import log


def get_message(response_type):
    """
    Return a message from a smalltalk intent.
    :param response_type LUIS response.
    """
    with open('hackupc/bienebot/responses/smalltalk/smalltalk_data.json') as json_data:
        data = json.load(json_data)

        intent = response_type['topScoringIntent']['intent']
        list_intent = intent.split('.')

        # Log stuff
        log.debug(f'|RESPONSE| Looking for [{list_intent[1]}] from JSON element')

        array = [random.choice(data[list_intent[1]])]
        return array

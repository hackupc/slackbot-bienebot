import json
import random

from hackupc.bienebot.util import log


def get_message(response_type):
    """
    Return a message from a meals intent
    :param response_type luis response
    """
    with open('hackupc/bienebot/responses/meals/meals_data.json') as json_data:
        data = json.load(json_data)

        intent = response_type['topScoringIntent']['intent']
        list_intent = intent.split('.')

        # Log stuff
        log.info('|RESPONSE| Looking for [{}] from JSON element'.format(list_intent[1]))

        if list_intent[1] == 'Help' or list_intent[1] == 'Schedule':
            array = ['\n'.join(data[list_intent[1]])]
        else:
            array = [random.choice(data[list_intent[1]])]

        return array

import json
import random

from hackupc.bienebot.util import log


def get_message(response_type):
    """
    Return a message from a projects intent
    :param response_type luis response
    """
    with open('hackupc/bienebot/responses/hardware_lab/hardware_lab_data.json') as json_data:
        data = json.load(json_data)

        intent = response_type['topScoringIntent']['intent']
        list_intent = intent.split('.')

        # Log stuff
        log.info('|RESPONSES| Looking for [{}] from JSON element'.format(list_intent[1]))

        array = [random.choice(data[list_intent[2]])]
        return array

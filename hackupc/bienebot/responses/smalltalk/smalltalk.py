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

        prediction = response_type['prediction']

        entities = prediction['entities']

        smalltalk_type = entities.get('SmalltalkType', [['Other']])[0][0]

        # Log stuff
        log.debug(f'|RESPONSE| Looking for [{smalltalk_type}] from JSON element')

        array = [random.choice(data[smalltalk_type])]
        return array

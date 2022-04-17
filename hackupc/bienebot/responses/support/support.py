import json
import random

from hackupc.bienebot.util import log


def get_message(response_type):
    """
    Return a message from a support intent.
    :param response_type LUIS response.
    """
    with open('hackupc/bienebot/responses/support/support_data.json') as json_data:
        data = json.load(json_data)

        prediction = response_type['prediction']

        entities = prediction['entities']

        support_type = entities.get('SupportType', [['Contact']])[0][0]

        # Log stuff
        log.debug(f'|RESPONSE| Looking for [{support_type}] from JSON element')

        array = [random.choice(data[support_type])]
        return array

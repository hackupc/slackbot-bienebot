import json
import random

from hackupc.bienebot.responses.error import error
from hackupc.bienebot.util import log


def get_message(response_type):
    """
    Return a message from a Hardware Lab intent.
    :param response_type LUIS response.
    """
    with open('hackupc/bienebot/responses/hardware_lab/hardware_lab_data.json') as json_data:
        data = json.load(json_data)

        prediction = response_type['prediction']

        entities = prediction['entities']

        question_type = entities.get('QuestionType', [['Error']])[0][0]

        # Log stuff
        log.debug(f'|RESPONSE| Looking for [{question_type}] from JSON element')

        if question_type == 'List':
            array = ['\n'.join(data['List'])]
        elif question_type == 'error':
            array = [error.get_message()]
        else:
            array = [random.choice(data[question_type])]
        return array

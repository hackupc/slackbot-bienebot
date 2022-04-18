import json
import random

from hackupc.bienebot.util import log


ACCEPTED_QUESTION_TYPES = ['Exist', 'Help', 'How', 'Which']


def get_message(response_type):
    """
    Return a message from a Hardware Lab intent.
    :param response_type LUIS response.
    """
    with open('hackupc/bienebot/responses/hardware_lab/hardware_lab_data.json') as json_data:
        data = json.load(json_data)

        prediction = response_type['prediction']

        entities = prediction['entities']

        question_type = entities.get('QuestionType', [['Which']])[0][0]

        if question_type not in ACCEPTED_QUESTION_TYPES:
            question_type = 'How'

        # Log stuff
        log.debug(f'|RESPONSE| Looking for [{question_type}] from JSON element')

        if question_type == 'Which':
            array = ['\n'.join(data['Which'])]
        else:
            array = [random.choice(data[question_type])]
        return array

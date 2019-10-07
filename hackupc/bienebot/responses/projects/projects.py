import json
import random

from hackupc.bienebot.util import log


def get_message(response_type):
    """
    Return a message from a projects intent.
    :param response_type LUIS response.
    """
    with open('hackupc/bienebot/responses/projects/projects_data.json') as json_data:
        data = json.load(json_data)

        intent = response_type['topScoringIntent']['intent']
        list_intent = intent.split('.')

        # Log stuff
        log.info(f'|RESPONSE| Looking for [{list_intent[1]}] from JSON element')

        if list_intent[1] == 'Help':
            array = help_project(data)
        else:
            array = [random.choice(data[list_intent[1]])]

        return array


def help_project(data):
    """
    Retrieve response for `help` question.
    :param data: Data.
    :return: Array of responses.
    """
    return ['\n'.join(data['Help'])]

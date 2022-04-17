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

        prediction = response_type['prediction']

        entities = prediction['entities']

        project_question = entities.get('ProjectQuestion', [['Help']])[0][0]

        # Log stuff
        log.debug(f'|RESPONSE| Looking for [{project_question}] from JSON element')

        if project_question == 'Help':
            array = help_project(data)
        else:
            array = [random.choice(data[project_question])]

        return array


def help_project(data):
    """
    Retrieve response for `help` question.
    :param data: Data.
    :return: Array of responses.
    """
    return ['\n'.join(data['Help'])]

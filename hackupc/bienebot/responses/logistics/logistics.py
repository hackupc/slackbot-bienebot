import json

from hackupc.bienebot.responses.error import error
from hackupc.bienebot.util import log

ACCEPTED_QUESTION_TYPES = ['Where', 'When', 'How']


def get_message(response_type):
    """
    Return a message from a logistics intent.
    :param response_type LUIS response.
    """
    with open('hackupc/bienebot/responses/logistics/logistics_data.json') as json_data:
        data = json.load(json_data)

        prediction = response_type['prediction']

        entities = prediction['entities']

        question_type = entities.get('QuestionType', [['']])[0][0]

        logistics = entities.get('Logistic', [['']])[0][0]

        switcher = {
            'How': how,
            'When': when,
            'Where': where
        }
        # Get the function from switcher dictionary
        func = switcher.get(question_type, lambda: error.get_message())
        # Execute the function
        return func(data, logistics)


def how(data, logistic):
    """
    Retrieve response for `how` question given a list of entities.
    :param data: Data.
    :param logistic: logistic.
    :return: Array of responses.
    """
    array = []
    if logistic:
        log.debug(f'|RESPONSE|: About [{logistic}] getting HOW')
        array.append(data['logistic'][logistic]['how'])
    else:
        array.append(data['default']['how'])
    return array


def when(data, logistic):
    """
    Retrieve response for `when` question given a list of entities.
    :param data: Data.
    :param logistic: logistic.
    :return: Array of responses.
    """
    array = []
    if logistic:
        log.debug(f'|RESPONSE|: About [{logistic}] getting WHEN')
        array.append(data['logistic'][logistic]['when'])
    else:
        array.append(data['default']['when'])
    return array


def where(data, logistic):
    """
    Retrieve response for `where` question given a list of entities.
    :param data: Data.
    :param logistic: logistic.
    :return: Array of responses.
    """
    array = []
    if logistic:
        log.debug(f'|RESPONSE|: About [{logistic}] getting WHERE')
        array.append(data['logistic'][logistic]['where'])
        array.append(data['default']['more'])
    else:
        array.append(data['default']['where'])
        array.append(data['default']['more'])
    return array

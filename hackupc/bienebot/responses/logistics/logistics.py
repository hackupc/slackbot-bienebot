import json

from hackupc.bienebot.responses.error import error
from hackupc.bienebot.util import log


def get_message(response_type):
    """
    Return a message from a logistics intent.
    :param response_type LUIS response.
    """
    with open('hackupc/bienebot/responses/logistics/logistics_data.json') as json_data:
        data = json.load(json_data)

        intent = response_type['topScoringIntent']['intent']
        list_intent = intent.split('.')

        entities = response_type['entities']

        # Log stuff
        if entities:
            entity = entities[0]['entity']
            log_info = f'|RESPONSE| About [{entity}] getting [{list_intent[1]}]'
        else:
            log_info = '|RESPONSE| No entities about logistics'
        log.debug(log_info)

        switcher = {
            'How': how,
            'When': when,
            'Where': where
        }
        # Get the function from switcher dictionary
        func = switcher.get(list_intent[1], lambda: error.get_message())
        # Execute the function
        return func(data, entities)


def how(data, entities):
    """
    Retrieve response for `how` question given a list of entities.
    :param data: Data.
    :param entities: Entities.
    :return: Array of responses.
    """
    array = []
    if entities:
        logistic = entities[0]['resolution']['values'][0].lower()
        log.debug(f'|RESPONSE|: About [{logistic}] getting HOW')
        array.append(data['logistic'][logistic]['how'])
    else:
        array.append(data['default']['how'])
    return array


def when(data, entities):
    """
    Retrieve response for `when` question given a list of entities.
    :param data: Data.
    :param entities: Entities.
    :return: Array of responses.
    """
    array = []
    if entities:
        logistic = entities[0]['resolution']['values'][0].lower()
        log.debug(f'|RESPONSE|: About [{logistic}] getting WHEN')
        array.append(data['logistic'][logistic]['when'])
    else:
        array.append(data['default']['when'])
    return array


def where(data, entities):
    """
    Retrieve response for `where` question given a list of entities.
    :param data: Data.
    :param entities: Entities.
    :return: Array of responses.
    """
    array = []
    if entities:
        logistic = entities[0]['resolution']['values'][0].lower()
        log.debug(f'|RESPONSE|: About [{logistic}] getting WHERE')
        array.append(data['logistic'][logistic]['where'])
        array.append(data['default']['more'])
    else:
        array.append(data['default']['where'])
        array.append(data['default']['more'])
    return array

import json

from hackupc.bienebot.responses.error import error
from hackupc.bienebot.util import log


def get_message(response_type):
    """
    Return a message from a logistics intent
    :param response_type luis response
    """
    with open('hackupc/bienebot/responses/logistics/logistics_data.json') as json_data:
        data = json.load(json_data)

        intent = response_type['topScoringIntent']['intent']
        list_intent = intent.split('.')

        entities = response_type['entities']

        # Log stuff
        if entities:
            log_info = '|RESPONSE| About [{}] getting [{}]'.format(entities[0]['entity'], list_intent[1])
        else:
            log_info = '|RESPONSE| No entities about logistics'
        log.info(log_info)

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
    array = []
    if entities:
        logistic = entities[0]['resolution']['values'][0].lower()
        log.info('|RESPONSE|: About [{}] getting HOW'.format(logistic))
        array.append(data['logistic'][logistic]['how'])
    else:
        array.append(data['default']['how'])
    return array


def when(data, entities):
    array = []
    if entities:
        logistic = entities[0]['resolution']['values'][0].lower()
        log.info('|RESPONSE|: About [{}] getting WHEN'.format(logistic))
        array.append(data['logistic'][logistic]['when'])
    else:
        array.append(data['default']['when'])
    return array


def where(data, entities):
    array = []
    if entities:
        logistic = entities[0]['resolution']['values'][0].lower()
        log.info('|RESPONSE|: About [{}] getting WHERE'.format(logistic))
        array.append(data['logistic'][logistic]['where'])
        array.append(data['default']['more'])
    else:
        array.append(data['default']['where'])
        array.append(data['default']['more'])
    return array

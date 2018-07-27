import json

from hackupc.bienebot.responses.error import error
from hackupc.bienebot.util import log


# noinspection PyBroadException
def get_message(response_type):
    """
    Return a message from a sponsor intent
    :param response_type luis response
    """
    with open('hackupc/bienebot/responses/sponsors/sponsors_data.json') as json_data:
        data = json.load(json_data)

        intent = response_type['topScoringIntent']['intent']
        list_intent = intent.split('.')
        entities = response_type['entities']

        # Log stuff
        if entities:
            log_info = '|RESPONSE| About [{}] getting [{}]'.format(entities[0]['entity'], list_intent[1])
        else:
            log_info = '|RESPONSE| Getting [{}] about all sponsors'.format(list_intent[1])
        log.info(log_info)

        switcher = {
            'Which': which,
            'Where': where,
            'Challenge': challenge
        }
        # Get the function from switcher dictionary
        func = switcher.get(list_intent[1], lambda: error.get_message())
        # Execute the function
        return func(data, entities)


# noinspection PyUnusedLocal
def which(data, entities):
    response = '{}\n'.format(data['default']['total'])
    for value in data['sponsors'].values():
        response += '- {}\n'.format(value['name'])
    return response


def where(data, entities):
    if entities:
        sponsor = entities[0]['entity'].lower()
        log.info('|RESPONSE|: About [{}] getting WHERE'.format(sponsor))
        return data['sponsors'][sponsor]['where']
    else:
        return data['default']['where']


def challenge(data, entities):
    if entities:
        sponsor = entities[0]['entity'].lower()
        log.info('|RESPONSE|: About [{}] getting CHALLENGE'.format(sponsor))
        return data['sponsors'][sponsor]['challenge']
    else:
        return data['default']['challenge']

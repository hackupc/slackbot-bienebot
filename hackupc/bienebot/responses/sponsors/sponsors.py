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
            'Challenge': challenge,
            'Help': help_sponsor,
            'Contact': contact
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
    array = [response]
    return array


def where(data, entities):
    array = []
    if entities:
        sponsor = entities[0]['entity'].lower()
        log.info('|RESPONSE|: About [{}] getting WHERE'.format(sponsor))
        array.append(data['sponsors'][sponsor]['where'])
    else:
        array.append(data['default']['where'])
    return array


def challenge(data, entities):
    array = []
    if entities:
        sponsor = entities[0]['entity'].lower()
        log.info('|RESPONSE|: About [{}] getting CHALLENGE'.format(sponsor))
        array.append(data['sponsors'][sponsor]['challenge'])
    else:
        array.append(data['default']['challenge'])
    return array


# noinspection PyUnusedLocal
def help_sponsor(data, entities):
    return data['help']


def contact(data, entities):
    array = []
    if entities:
        sponsor = entities[0]['entity'].lower()
        log.info('|RESPONSE|: About [{}] getting CONTACT'.format(sponsor))
        array.append(data['sponsors'][sponsor]['contact'])
    else:
        array.append(data['default']['contact'])
    return array

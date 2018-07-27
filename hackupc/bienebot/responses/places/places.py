import json

from hackupc.bienebot.responses.error import error
from hackupc.bienebot.util import log


# noinspection PyBroadException
def get_message(response_type):
    """
    Return a message from a sponsor intent
    :param response_type luis response
    """
    with open('hackupc/bienebot/responses/places/places_data.json') as json_data:
        data = json.load(json_data)

        intent = response_type['topScoringIntent']['intent']
        list_intent = intent.split('.')

        entities = response_type['entities']

        # Log stuff
        if entities:
            log_info = '|RESPONSE| About [{}] getting [{}]'.format(entities[0]['entity'], list_intent[1])
        else:
            log_info = '|RESPONSE| No entities about places'
        log.info(log_info)

        switcher = {
            'When': when,
            'Where': where,
        }
        # Get the function from switcher dictionary
        func = switcher.get(list_intent[2], lambda: error.get_message())
        # Execute the function
        return func(data, entities)


def where(data, entities):
    if entities:
        place = entities[0]['entity'].lower()
        log.info('|RESPONSE|: About [{}] getting WHERE'.format(place))
        return data['places'][place]['where']
    else:
        return data['default']['where']


def when(data, entities):
    if entities:
        place = entities[0]['entity'].lower()
        log.info('|RESPONSE|: About [{}] getting WHEN'.format(place))
        return data['places'][place]['when']
    else:
        return data['default']['when']

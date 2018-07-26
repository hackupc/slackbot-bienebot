import json
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

        try:
            switcher = {
                'When': when,
                'Where': where,
            }
            # Get the function from switcher dictionary
            func = switcher.get(list_intent[2], lambda: "No understand")
            # Execute the function
            return func(data, intent, entities)

        except Exception:
            return "Don't understand"


def where(data, intent, entities):
    try:
        place = entities[0]['entity'].lower()

        log.info('|RESPONSE|: About [' + place + '] getting WHERE')
        return data['places'][place]['where']

    except Exception:
        return data['default']['where']

def when(data, intent, entities):
    try:
        place = entities[0]['entity'].lower()

        log.info('|RESPONSE|: About [' + place + '] getting WHEN')
        return data['places'][place]['when']
    except Exception:
        return data['default']['when']

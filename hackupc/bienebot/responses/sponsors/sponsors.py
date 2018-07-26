import json
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

        try:
            switcher = {
                'Which': which,
                'Where': where,
                'Challenge':challenge
            }
            # Get the function from switcher dictionary
            func = switcher.get(list_intent[1], lambda: "No understand")
            # Execute the function
            return func(data, intent, entities)

        except Exception:
            return "Don't understand"


def which(data, intent, entities):
    log.info('|RESPONSE|: Know all the sponsors')
    response = data['default']['total'] + '\n'
    for key, value in data['sponsors'].items():
        response = response + '- ' + value['name'] + '\n'
    return response;


def where(data, intent, entities):
    sponsor = entities[0]['entity'].lower()
    log.info('|RESPONSE|: About [' + sponsor + '] getting WHERE')
    return data['sponsors'][sponsor]['where']

def challenge(data, intent, entities):
    sponsor = entities[0]['entity'].lower()
    log.info('|RESPONSE|: About [' + sponsor + '] getting CHALLENGE')
    return data['sponsors'][sponsor]['nothing']

import json


# noinspection PyBroadException
def get_message(response_type):
    """
    Return a message from a sponsor intent
    :param response_type luis response
    """
    with open('hackupc/bienebot/responses/sponsors/sponsors_data.json') as f:
        data = json.load(f)

        intent = response_type['topScoringIntent']['intent']
        list_intent = intent.split('.')

        entities = response_type['entities']

        try:
            switcher = {
                'Which': which,
                'Where': where
            }
            # Get the function from switcher dictionary
            func = switcher.get(list_intent[1], lambda: "No understand")
            # Execute the function
            return func(data, intent, entities)

        except Exception:
            return "Don't understand"


def which(data, intent, entities):
    return data['which']


def where(data, intent, entities):
    sponsor = entities[0]['entity']
    return data['where'][sponsor]

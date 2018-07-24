import random, json
from hackupc.bienebot.responses.sponsors import sponsors_data


def get_message(response_type):
    """
    Return a message from a sponsor intent
    """
    with open('sponsors_data.json') as f:
        data = json.load(f)

    intent = response_data['topScoringIntent']['intent']
    entities = response_data['entities']
    list_intent = intent.split('.')

    switcher = {
        'which': which,
        'where': where
    }
    # Get the function from switcher dictionary
    func = switcher.get(list_intent[1], lambda: "No understand" )
    # Execute the function
    return func(data,intent,entities)

def which(data,intent,entities):
    return data['which']

def where(data,intent,entities):
    sponsor = entities['0']['entity']
    return data['where'][sponsor]

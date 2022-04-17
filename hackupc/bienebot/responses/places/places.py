import json

from hackupc.bienebot.responses.error import error
from hackupc.bienebot.util import log


def get_message(response_type):
    """
    Return a message from a sponsor intent.
    :param response_type LUIS response.
    """
    with open('hackupc/bienebot/responses/places/places_data.json') as json_data:
        data = json.load(json_data)

        prediction = response_type['prediction']

        entities = prediction['entities']

        question_type = entities['QuestionType'][0][0]

        place = entities.get('Place', [['']])[0][0]

        switcher = {
            'When': when,
            'Where': where,
            'Help': help_place
        }
        # Get the function from switcher dictionary
        func = switcher.get(question_type, help_place if not place else where)
        # Execute the function
        return func(data, place)


def where(data, place):
    """
    Retrieve response for `where` question given a list of entities
    :param data: Data.
    :param place: place.
    :return: Array of responses.
    """
    array = []
    if place:
        log.debug(f'|RESPONSE|: About [{place}] getting WHERE')
        array.append(data['places'][place]['where'])
        array.append(data['default']['more'])
    else:
        array.append(data['default']['where'])
        array.append(data['default']['more'])
    return array


def when(data, place):
    """
    Retrieve response for `when` question given a list of entities.
    :param data: Data.
    :param place: place.
    :return: Array of responses.
    """
    array = []
    if place:
        log.debug(f'|RESPONSE|: About [{place}] getting WHEN')
        array.append(data['places'][place]['when'])
    else:
        array.append(data['default']['when'])
    return array


# noinspection PyUnusedLocal
def help_place(data, place):
    """
    Retrieve response for `help` question given a list of entities.
    :param data: Data.
    :param place: place.
    :return: Array of responses.
    """
    return ['\n'.join(data['help'])]

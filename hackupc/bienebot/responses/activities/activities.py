import json

from hackupc.bienebot.responses.error import error
from hackupc.bienebot.util import log


def get_message(response_type):
    """
    Return a message from a activities intent.
    :param response_type LUIS response.
    """
    with open('hackupc/bienebot/responses/activities/activities_data.json') as json_data:
        data = json.load(json_data)

        intent = response_type['topScoringIntent']['intent']
        list_intent = intent.split('.')

        entities = response_type['entities']

        # Log stuff
        if entities:
            entity = entities[0]['entity']
            log_info = f'|RESPONSE| About [{entity}] getting [{list_intent[1]}]'
        else:
            log_info = '|RESPONSE| No entities about activities'
        log.debug(log_info)

        switcher = {
            'What': what,
            'When': when,
            'Where': where,
            'Which': which_activity,
            'Help': help_activity
        }
        # Get the function from switcher dictionary
        func = switcher.get(list_intent[2], lambda: error.get_message())
        # Execute the function
        return func(data, entities)


def what(data, entities):
    """
    Retrieve response for `what` question given a list of entities.
    :param data: Data.
    :param entities: Entities.
    :return: Array of responses.
    """
    array = []
    if entities:
        activity = entities[0]['resolution']['values'][0].lower()
        log.debug(f'|RESPONSE|: About [{activity}] getting WHAT')
        array.append(data['activities'][activity]['what'])
    else:
        array.append(data['default']['what'])
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
        activity = entities[0]['resolution']['values'][0].lower()
        log.debug(f'|RESPONSE|: About [{activity}] getting WHEN')
        array.append(data['activities'][activity]['when'])
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
        activity = entities[0]['resolution']['values'][0].lower()
        log.debug(f'|RESPONSE|: About [{activity}] getting WHERE')
        array.append(data['activities'][activity]['where'])
        array.append(data['default']['more'])
    else:
        array.append(data['default']['where'])
        array.append(data['default']['more'])
    return array


# noinspection PyUnusedLocal
def which_activity(data, entities):
    """
    Retrieve response for `which` question given a list of entities.
    :param data: Data.
    :param entities: Entities.
    :return: Array of responses,
    """
    return ['\n'.join(data['which'])]


# noinspection PyUnusedLocal
def help_activity(data, entities):
    """
    Retrieve response for `help` question given a list of entities.
    :param data: Data.
    :param entities: Entities.
    :return: Array of responses,
    """
    return data['help']

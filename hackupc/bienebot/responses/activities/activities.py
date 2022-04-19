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

        prediction = response_type['prediction']

        entities = prediction['entities']

        question_type = entities.get('QuestionType', [['']])[0][0]

        activity = entities.get('Activity', [['']])[0][0]

        switcher = {
            'What': what,
            'When': when,
            'Where': where,
            'Which': which_activity,
            'Help': help_activity
        }
        # Get the function from switcher dictionary
        func = switcher.get(question_type, what if activity else help_activity)
        # Execute the function
        return func(data, activity)


def what(data, activity):
    """
    Retrieve response for `what` question given a list of entities.
    :param data: Data.
    :param activity: Activity.
    :return: Array of responses.
    """
    array = []
    if activity:
        log.debug(f'|RESPONSE|: About [{activity}] getting WHAT')
        array.append(data['activities'][activity]['what'])
    else:
        array.append(data['default']['what'])
    return array


def when(data, activity):
    """
    Retrieve response for `when` question given a list of entities.
    :param data: Data.
    :param activity: Activity.
    :return: Array of responses.
    """
    array = []
    if activity:
        log.debug(f'|RESPONSE|: About [{activity}] getting WHEN')
        array.append(data['activities'][activity]['when'])
    else:
        array.append(data['default']['when'])
    return array


def where(data, activity):
    """
    Retrieve response for `where` question given a list of entities.
    :param data: Data.
    :param activity: Activity.
    :return: Array of responses.
    """
    array = []
    if activity:
        log.debug(f'|RESPONSE|: About [{activity}] getting WHERE')
        array.append(data['activities'][activity]['where'])
        array.append(data['default']['more'])
    else:
        array.append(data['default']['where'])
        array.append(data['default']['more'])
    return array


# noinspection PyUnusedLocal
def which_activity(data, activity):
    """
    Retrieve response for `which` question given a list of entities.
    :param data: Data.
    :param activity: Activity.
    :return: Array of responses,
    """
    return ['\n'.join(data['which'])]


# noinspection PyUnusedLocal
def help_activity(data, activity):
    """
    Retrieve response for `help` question given a list of entities.
    :param data: Data.
    :param activity: Activity.
    :return: Array of responses,
    """
    return data['help']

import json
import random

from datetime import datetime, timedelta

from hackupc.bienebot import SCHEDULE_JSON_URL
from hackupc.bienebot.util import log, request

ACCEPTED_QUESTION_TYPES = ['Where', 'When']


def get_message(response_type):
    """
    Return a message from a hackUPC intent.
    :param response_type LUIS response.
    """
    with open('hackupc/bienebot/responses/hackupc/hackupc_data.json') as json_data:
        data = json.load(json_data)

        prediction = response_type['prediction']

        entities = prediction['entities']

        question_type = entities['QuestionType'][0][0]

        if question_type not in ACCEPTED_QUESTION_TYPES:
            question_type = 'schedule'

        # Log stuff
        log.debug(f'|RESPONSE| Looking for [{question_type}] from JSON element')

        array = [random.choice(data[question_type])]

        return array


# No use
def next_hackupc():
    """
    Get next event calling live JSON.
    :return: Next event message.
    """
    now = datetime.utcnow() + timedelta(hours=2)
    params = {'date': now.time()}
    response = request.execute('GET', SCHEDULE_JSON_URL, params=params)

    # Per each day
    for day in response['days']:
        day_date = datetime.strptime(day['date'], '%d/%m/%Y')
        if now.date() <= day_date.date():
            for event in day['events']:
                event_date = datetime.strptime('{} {}'.format(day['date'], event['startHour']), '%d/%m/%Y %H:%M')
                if now <= event_date:
                    return [
                        'The following event is called `{}` located at `{}`. {}. It starts at `{}` and ends at `{}`.'
                        .format(
                            event['title'],
                            event['locationName'],
                            event['description'],
                            event['startHour'],
                            event['endHour']
                        )
                    ]

    # No more activities response
    return ['There are not more activities in this edition of HackUPC :hackupc: So excited to see you again next year!']

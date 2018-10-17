import json
import random
import requests

from datetime import datetime, timedelta

from hackupc.bienebot.util import log


def get_message(response_type):
    """
    Return a message from a hackUPC intent
    :param response_type luis response
    """
    with open('hackupc/bienebot/responses/hackupc/hackupc_data.json') as json_data:
        data = json.load(json_data)

        intent = response_type['topScoringIntent']['intent']
        list_intent = intent.split('.')

        # Log stuff
        log.info('|RESPONSE| Looking for [{}] from JSON element'.format(list_intent[1]))

        if list_intent[1] == 'Next':
            array = next_hackupc()
        elif list_intent[1] == 'Schedule':
            array = ['\n'.join(data['Schedule'])]
        else:
            array = [random.choice(data[list_intent[1]])]

        return array


def next_hackupc():
    """
    Get next event calling Live json
    :return: response
    """
    now = datetime.utcnow() + timedelta(hours=2)
    params = {
        'date': now.time()
    }
    response = requests.get(url='https://hackupc.com/assets/data/schedule.json', params=params, timeout=5)
    response_dict = response.json()

    # Per each day
    for day in response_dict['days']:
        day_date = datetime.strptime(day['date'], '%d/%m/%Y')
        if now.date() <= day_date.date():
            for event in day['events']:
                event_date = datetime.strptime('{} {}'.format(day['date'], event['startHour']), '%d/%m/%Y %H:%M')
                if now <= event_date:
                    return ['The following event is called `{}` located at `{}`. {}. It starts at `{}` and ends at `{}`.'
                            .format(
                                    event['title'],
                                    event['locationName'],
                                    event['description'],
                                    event['startHour'],
                                    event['endHour']
                            )]

    # No more activities response
    return ['There are not more activities in this edition of HackUPC :hackupc: So excited to see you again next year!']

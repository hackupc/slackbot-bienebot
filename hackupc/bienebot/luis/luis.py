import requests

from hackupc.bienebot import *
from hackupc.bienebot.util import log
from hackupc.bienebot.responses import responses


def get_intent(query):
    headers = {
        'Ocp-Apim-Subscription-Key': LUIS_SUBSCRIPTION_KEY,
    }

    params = {
        'q': query,
        'timezoneOffset': '0',
        'verbose': 'false',
        'spellCheck': 'false',
        'staging': 'false',
    }

    try:
        r = requests.get('https://' + LUIS_SERVER + '/luis/v2.0/apps/' + LUIS_ID, headers=headers, params=params)
        response_data = r.json()
        answer = analyze_response(response_data)
        return answer
    except Exception as e:
        log.error(e)


def analyze_response(response_data):
    intent = response_data['topScoringIntent']['intent']
    if intent.startswith('Sponsors'):
        return responses.sponsors.sponsors.analyze(response_data)
    else:
        return 'Don\'t understand'

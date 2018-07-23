import requests

from hackupc.bienebot import *
from hackupc.bienebot.util import log


def get_intent(query):
    """
    Get intent from LUIS
    :param query: query
    :return: LUIS answer
    """
    log.info('|LUIS| Get intent with query [{}]'.format(query))
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
        url = 'https://{}/luis/v2.0/apps/{}'.format(LUIS_SERVER, LUIS_ID)
        r = requests.get(url=url, headers=headers, params=params)
        response_data = r.json()
        answer = analyze_response(response_data)
        log.info('|LUIS| After analyzing data, we got [{}]'.format(answer))
        return answer
    except Exception as e:
        log.error(e)


def analyze_response(response_data):
    """
    Analyze LUIS response
    :param response_data: response data
    :return: response analyzed
    """
    intent = response_data['topScoringIntent']['intent']
    log.info('|LUIS| Intent that we got [{}]'.format(intent))
    if intent.startswith('Sponsors'):
        return 'Hello'
    else:
        return 'Don\'t understand'

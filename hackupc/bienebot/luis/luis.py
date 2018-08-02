from hackupc.bienebot import *
from hackupc.bienebot.responses.error import error
from hackupc.bienebot.util import log, request
from hackupc.bienebot.responses.sponsors import sponsors
from hackupc.bienebot.responses.smalltalk import smalltalk
from hackupc.bienebot.responses.places import places
from hackupc.bienebot.responses.projects import projects
from hackupc.bienebot.responses.support import support


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
        r = request.execute(method='GET', url=url, headers=headers, params=params)
        response_data = r.json()
        answers = analyze_response(response_data)
        for an in answers:
            log.info('|LUIS| After analyzing data, we got [{}]'.format(an.replace('\n', '')))
        return answers, response_data['topScoringIntent']['intent']
    except Exception as e:
        log.error(e)


def analyze_response(response_data):
    """
    Analyze LUIS response
    :param response_data: response data
    :return: response analyzed
    """
    try:
        intent = response_data['topScoringIntent']['intent']
        log.info('|LUIS| Intent that we got [{}]'.format(intent))

        answer = []

        if intent.startswith('Sponsors'):
            answer = sponsors.get_message(response_data)
        elif intent.startswith('Indication.Place'):
            answer =  places.get_message(response_data)
        elif intent.startswith('Smalltalk'):
            answer =  smalltalk.get_message(response_data)
        elif intent.startswith('Project'):
            answer =  projects.get_message(response_data)
        elif intent.startswith('Support'):
            answer =  support.get_message(response_data)
        elif intent.startswith('Indication.Activity'):
            answer =  support.get_message(response_data)
        else:
            answer =  error.get_message()
        
        inp = response_data['query']
        if 'biene' in inp.lower() and not 'Smalltalk.Biene' in intent:
            log.info('|LUIS| BIENE detected')
            answer.append('BIENE')
        return array

    except Exception as e:
        log.error(e)
        return error.get_message()

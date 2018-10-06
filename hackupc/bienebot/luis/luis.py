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

        # Initialize answer array
        answer = list()

        if intent.startswith('Sponsors'):
            answer.append(sponsors.get_message(response_data))
        elif intent.startswith('Indication.Place'):
            answer.append(places.get_message(response_data))
        elif intent.startswith('Smalltalk'):
            answer.append(smalltalk.get_message(response_data))
        elif intent.startswith('Project'):
            answer.append(projects.get_message(response_data))
        elif intent.startswith('Support'):
            answer.append(support.get_message(response_data))
        elif intent.startswith('Indication.Activity'):
            answer.append(support.get_message(response_data))
        else:
            answer.append(error.get_message())
            return answer

        # Check for biene manually
        query_input = response_data['query']
        if 'biene' in query_input.lower() and 'Smalltalk.Biene' not in intent:
            log.info('|LUIS| BIENE detected')
            answer.append('BIENE')

        # Return array of answers
        return answer

    except Exception as e:
        log.error(e)
        return error.get_message()

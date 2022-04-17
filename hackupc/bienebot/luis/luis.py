import re

from hackupc.bienebot import *
from hackupc.bienebot.responses.activities import activities
from hackupc.bienebot.responses.error import error
from hackupc.bienebot.responses.hackupc import hackupc
from hackupc.bienebot.responses.hardware_lab import hardware_lab
from hackupc.bienebot.responses.logistics import logistics
from hackupc.bienebot.responses.meals import meals
from hackupc.bienebot.responses.mentor import mentor
from hackupc.bienebot.responses.sponsors import sponsors
from hackupc.bienebot.responses.smalltalk import smalltalk
from hackupc.bienebot.responses.places import places
from hackupc.bienebot.responses.projects import projects
from hackupc.bienebot.responses.support import support
from hackupc.bienebot.util import log, request


def get_intent(query):
    """
    Get intent from LUIS.
    :param query: Query to process.
    :return: LUIS answer.
    """
    query = re.sub(r':([a-zA-Z]|_)+:', '', query).strip()
    log.debug(f'|LUIS| Get intent with query [{query}]')
    # headers = {'Ocp-Apim-Subscription-Key': LUIS_SUBSCRIPTION_KEY}
    headers = {}
    params = {
        'query': query,
        'log': 'true',
        # 'timezoneOffset': '0',
        'verbose': 'false',
        # 'spellCheck': 'false',
        # 'staging': 'false',
        'show-all-intents': 'true',
        'subscription-key': LUIS_SUBSCRIPTION_KEY,
    }
    try:
        url = f'https://{LUIS_SERVER}/luis/prediction/v3.0/apps/{LUIS_ID}/slots/production/predict'
        response_data = request.execute(method='GET', url=url, headers=headers, params=params)
        answers = analyze_response(response_data)

        prediction = response_data['prediction']
        intent = prediction['topIntent']
        score = prediction['intents'][intent]['score']

        for an in answers:
            an = an.replace('\n', '')
            log.debug(f'|LUIS| After analyzing data, we got [{an}]')
        return answers, intent, score
    except Exception as e:
        log.exception(e)


def analyze_response(response_data):
    """
    Analyze LUIS response.
    :param response_data: Response data to analyze.
    :return: Response analyzed.
    """
    try:
        # Retrieve intent
        prediction = response_data['prediction']
        intent = prediction['topIntent']
        score = prediction['intents'][intent]['score']
        log.debug(f'|LUIS| Intent that we got [{intent}]')

        # Initialize answer array
        answer = list()

        # Check score
        if score < SCORE_THRESHOLD:
            answer.extend(error.get_message())
            return answer

        # Select intent
        if intent == 'Indication.Activity':
            answer.extend(activities.get_message(response_data))
        elif intent == 'HackUPC':
            answer.extend(hackupc.get_message(response_data))
        elif intent == 'HardwareLab':
            answer.extend(hardware_lab.get_message(response_data))
        elif intent == 'Logistics':
            answer.extend(logistics.get_message(response_data))
        elif intent == 'Meals':
            answer.extend(meals.get_message(response_data))
        elif intent == 'Mentor':
            answer.extend(mentor.get_message(response_data))
        elif intent == 'Indication.Place':
            answer.extend(places.get_message(response_data))
        elif intent == 'Project':
            answer.extend(projects.get_message(response_data))
        elif intent == 'Smalltalk':
            answer.extend(smalltalk.get_message(response_data))
        elif intent.startswith('Sponsors'):
            answer.extend(sponsors.get_message(response_data))
        elif intent == 'Support':
            answer.extend(support.get_message(response_data))
        else:
            if exists_biene(response_data):
                answer.extend(['BIENE'])
            else: 
                answer.extend(error.get_message())
            return answer

        # Check for biene manually
        if exists_biene(response_data):
            answer.extend(['BIENE'])

        # Return array of answers
        return answer

    except Exception as e:
        log.exception(e)
        return error.get_message()


def exists_biene(response_data):
    """
    Check if there's any biene in the response.
    :param response_data: Response data to check.
    :return: True if there is, False otherwise.
    """
    try:
        query_input = response_data['query']
        if 'biene' in query_input.lower():
            log.debug('|LUIS| BIENE detected')
            return True
        else:
            return False
    except Exception as e:
        log.exception(e)
        return False

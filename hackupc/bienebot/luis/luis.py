import requests
import json

from hackupc.bienebot import *



def LUIS_get_intent(query):

    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': LUIS_SUBSCRIPTION_KEY,
    }

    params ={
        # Query parameter
        'q': query,
        # Optional request parameters, set to default values
        'timezoneOffset': '0',
        'verbose': 'false',
        'spellCheck': 'false',
        'staging': 'false',
    }

    try:
        r = requests.get('https://' + LUIS_SERVER + '/luis/v2.0/apps/'+ LUIS_ID,headers=headers, params=params)
        response_data = r.json()
        answer = analyze_response(response_data);
        return answer;

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

def analyze_response(response_data):

    intent = response_data['topScoringIntent']['intent']
    if intent.startswith( 'Sponsors' ):
        return 'Hello'
    else:
        return 'Don\'t understad'

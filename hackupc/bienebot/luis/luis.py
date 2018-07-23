import requests

from hackupc.bienebot import *



def LUIS_get_intent(query):

    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': 'LUIS-SUBSCRIPTION-KEY',
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
        r = requests.get('https://' + 'LUIS-SERVER' + '/luis/v2.0/apps/'+ 'LUIS-ID',headers=headers, params=params)
        print(r.json())
        return r;

    except Exception as e:
        print("[Errno {0}] {1}".format(e.errno, e.strerror))

import json
import random

from hackupc.bienebot.util import log


def get_message(response_type):
    """
    Return a message from a meals intent.
    :param response_type LUIS response.
    """
    with open('hackupc/bienebot/responses/meals/meals_data.json') as json_data:
        data = json.load(json_data)

        prediction = response_type['prediction']

        entities = prediction['entities']

        meal_question = entities.get('MealQuestion', [['Help']])[0][0]

        # Log stuff
        log.debug(f'|RESPONSE| Looking for [{meal_question}] from JSON element')

        if meal_question == 'Help' or meal_question == 'Schedule':
            array = ['\n'.join(data[meal_question])]
        else:
            array = [random.choice(data[meal_question])]

        return array

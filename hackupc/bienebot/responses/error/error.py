import json
import random

from hackupc.bienebot.util import log


def get_message():
    """
    Return a message from a non understood question or error
    :return error response
    """

    with open('hackupc/bienebot/responses/error/error_data.json') as json_data:
        data = json.load(json_data)
        # Log stuff
        log.info('|RESPONSES| Looking for [error] from JSON element')
        return random.choice(data['No response'])

import json

from hackupc.bienebot.util import log


def get_message(response_type):
    """
    Return a message from a mentor intent.
    :param response_type LUIS response.
    """
    with open('hackupc/bienebot/responses/mentor/mentor_data.json') as json_data:
        data = json.load(json_data)

        # Log stuff
        log.debug(f'|RESPONSE| Looking for [Help] from JSON element')

        array = ['\n'.join(data['Help'])]
        return array

import random


def get_message(response_type):
    """
    Return a message from a sponsor intent
    """
    if response_type in chat_responses:
        return random.choice(chat_responses[response_type])
    return random.choice(chat_responses['no_answer'])

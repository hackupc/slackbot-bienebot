from slackclient import SlackClient

from hackupc.bienebot import *
from hackupc.bienebot.util import log

__slack_client = SlackClient(SLACK_API_TOKEN)


def get_slack():
    return __slack_client


def retrieve_message(slack_events):
    for event in slack_events:
        if event['type'] == 'message' and 'subtype' not in event:
            text = event['text']
            channel = event['channel']
            user = event['user']
            log.info('Retrieved the following message from user [{}] in channel [{}]: [{}]'.format(user, channel, text))
            return text, channel
    return None, None


def send_message(message, channel):
    log.info('Sent the following message in channel [{}]: [{}]'.format(channel, message))
    __slack_client.api_call(
        SLACK_API_METHOD,
        channel=channel,
        text=message
    )

# noinspection PyPackageRequirements
import slack
import multiprocessing as mp

from hackupc.bienebot import *
from hackupc.bienebot.luis import luis
from hackupc.bienebot.util import log


def get_rtm_client():
    """
    Initialize Slack RTM client.
    :return: RTM client.
    """
    return slack.RTMClient(token=SLACK_API_TOKEN, timeout=30)


def worker(message, channel, user, web_client):
    """
    Worker for interpreting the message from Slack.
    :param message: Message.
    :param channel: Channel.
    :param user: User.
    :param web_client: Slack web client.
    :return: Response sent.
    """
    # Biene in Random
    if channel == SLACK_API_RANDOM:
        if 'biene' in message.lower():
            send_message('BIENE', channel=channel, web_client=web_client)
    # Luis interaction
    else:
        response, intent, score = luis.get_intent(message)
        for mess in response:
            send_message(mess, channel=channel, web_client=web_client)
            log.save_activity(user, channel, intent, score, message, mess)


def send_message(message, channel=SLACK_API_CHANNEL, web_client=None):
    """
    Send message.
    :param message: Text to send.
    :param channel: Channel where send.
    :param web_client: Slack web client.
    :return: Message sent.
    """
    if not web_client:
        web_client = slack.WebClient(token=SLACK_API_TOKEN, timeout=30)
    log.info('|Slack| Sent the following message in channel [{}]: [{}]'.format(channel, message.replace('\n', '')))
    return web_client.chat_postMessage(channel=channel, text=message)


@slack.RTMClient.run_on(event='message')
def answer(**payload):
    """
    Retrieve messages.
    :return: Thread run.
    """
    if 'data' in payload:
        if all(x in payload['data'] for x in ['text', 'channel', 'user']):
            text = payload['data']['text']
            channel = payload['data']['channel']
            user = payload['data']['user']
            web_client = payload['web_client']
            log.info('|Slack| Retrieved the following message from user [{}] in channel [{}]: [{}]'.format(
                user, channel, text.replace('\n', ''))
            )
            # process = mp.Process(target=worker, args=(text, channel, user, web_client))
            # process.daemon = True
            # process.start()
            worker(text, channel, user, web_client)

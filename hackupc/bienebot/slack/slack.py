# noinspection PyPackageRequirements
import slack
import threading

from hackupc.bienebot import *
from hackupc.bienebot.luis import luis
from hackupc.bienebot.slack import commands
from hackupc.bienebot.util import log


def get_rtm_client():
    """
    Initialize Slack RTM client.
    :return: RTM client.
    """
    return slack.RTMClient(token=SLACK_API_TOKEN, timeout=30)


def manage_organizer_command(message, web_client, user):
    user_info = web_client.users_info(user=user)
    if not user_info.data.get('ok', False) or not user_info.data['user']['profile']['email'].endswith('@hackupc.com'):
        return False
    response = False
    if message.startswith('setprofile'):
        response = commands.set_profile(message, web_client, user=user)
    return response


def worker(message, channel, user, web_client):
    """
    Worker for interpreting the message from Slack.
    :param message: Message.
    :param channel: Channel.
    :param user: User.
    :param web_client: Slack web client.
    :return: Response sent.
    """
    if not message:
        return None
    # Biene in Random
    if channel == SLACK_API_RANDOM:
        if 'biene' in message.lower():
            send_message('BIENE', channel=channel, web_client=web_client)

    elif channel == SLACK_API_ORGANIZERS:
        try:
            response = manage_organizer_command(message=message.lower(), web_client=web_client, user=user)
            if response:
                send_message('Photo sent!', channel=channel, web_client=web_client)
        except Exception:
            send_message('Error', channel=channel, web_client=web_client)
    # Luis interaction
    elif SLACK_API_ACTIVE:
        response, intent, score = luis.get_intent(message)
        for mess in response:
            send_message(mess, channel=channel, web_client=web_client)
            log.save_activity(user, channel, intent, score, message, mess)


def send_message(message, channel=SLACK_API_ORGANIZERS, web_client=None):
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
        if all(x in payload['data'] for x in ['text', 'channel', 'user']) and 'thread_ts' not in payload['data']:
            text = payload['data']['text']
            channel = payload['data']['channel']
            user = payload['data']['user']
            web_client = payload['web_client']
            log.debug('|Slack| Retrieved the following message from user [{}] in channel [{}]: [{}]'.format(
                user, channel, text.replace('\n', ''))
            )
            thread = threading.Thread(target=worker, args=(text, channel, user, web_client))
            thread.daemon = True
            thread.start()

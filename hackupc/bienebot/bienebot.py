import time
import multiprocessing as mp

from hackupc.bienebot import *
from hackupc.bienebot.luis import luis
from hackupc.bienebot.slack.slack import Slack
from hackupc.bienebot.util import log


def run():
    """
    Run Biene Bot.
    :return: Biene bot ran
    """
    slack = Slack()
    try:
        if slack.rtm_connect():
            log.info('|BIENE| Biene Bot connected and running!')
            slack.notify(':bee: Biene Bot connected and running!')
            while True:
                message, channel, user = slack.retrieve_message()
                if message:
                    process = mp.Process(target=worker, args=(message, channel, user, slack,))
                    process.daemon = True
                    process.start()
                time.sleep(RTM_READ_DELAY)
        else:
            log.error('Connection failed. Exception traceback printed above.', slack)
    except Exception as e:
        log.error(e, slack)
    finally:
        log.info('|BIENE| Biene Bot stopped!')
        slack.notify(':bee: Biene Bot stopped!')
        return


def worker(message, channel, user, slack):
    """
    Worker for interpreting the message from Slack
    :param message: message
    :param channel: channel
    :param user: user
    :param slack: slack instance
    :return: response sent
    """
    # Biene in Random
    if channel == SLACK_API_RANDOM:
        if 'biene' in message.lower():
            slack.send_message('BIENE', channel)
    # Luis interaction
    else:
        response, intent, score = luis.get_intent(message)
        for mess in response:
            slack.send_message(mess, channel)
            log.save_activity(user, channel, intent, score, message, mess)

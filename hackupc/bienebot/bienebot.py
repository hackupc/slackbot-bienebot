import time

from hackupc.bienebot import *
from hackupc.bienebot.luis import luis
from hackupc.bienebot.slack.slack import Slack
from hackupc.bienebot.util import log


def run_bienebot():
    """
    Run Biene Bot
    :return: biene bot ran
    """
    slack = Slack()
    try:
        if slack.rtm_connect():
            log.info('|BIENE| Biene Bot connected and running!')
            slack.notify(':bee: Biene Bot connected and running!')
            while True:
                message, channel, user = slack.retrieve_message()
                if message:
                    response, intent = luis.get_intent(message)
                    slack.send_message(response, channel)
                    log.save_activity(user, channel, intent, message, response)
                time.sleep(RTM_READ_DELAY)
        else:
            log.error('Connection failed. Exception traceback printed above.')
    except Exception as e:
        log.error(e)
    finally:
        log.info('|BIENE| Biene Bot stopped!')
        slack.notify(':bee: Biene Bot stopped!')

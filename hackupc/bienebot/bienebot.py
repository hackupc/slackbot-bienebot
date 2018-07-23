import time

from hackupc.bienebot import *
from hackupc.bienebot.luis import luis
from hackupc.bienebot.slack import slack
from hackupc.bienebot.util import log


def run_bienebot():
    slack_client = slack.get_slack()
    if slack_client.rtm_connect(with_team_state=False):
        log.info('Starter Bot connected and running!')
        while True:
            message, channel = slack.retrieve_message(slack_client.rtm_read())
            if message:
                response = luis.get_intent(message)
                slack.send_message(response, channel)
            time.sleep(RTM_READ_DELAY)
    else:
        log.error('Connection failed. Exception traceback printed above.')

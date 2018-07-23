from slackclient import SlackClient

from hackupc.bienebot import *


class SlackSender:

    def __init__(self):
        self.slack = SlackClient(SLACK_API_TOKEN)


# Slack API object
slack = SlackSender()

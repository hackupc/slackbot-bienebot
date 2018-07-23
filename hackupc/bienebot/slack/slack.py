from slackclient import SlackClient

from hackupc.bienebot import *
from hackupc.bienebot.util import log, count


class Slack:

    def __init__(self):
        self.client = SlackClient(SLACK_API_TOKEN)

    def rtm_connect(self):
        """
        Connects to the RTM web socket
        :return: true if it's connected successfully, false otherwise
        """
        return self.client.rtm_connect(with_team_state=False)

    def retrieve_message(self):
        """
        Retrieve messages
        :return: text and channel message
        """
        for event in self.client.rtm_read():
            if event['type'] == 'message' and 'subtype' not in event:
                text = event['text']
                channel = event['channel']
                user = event['user']
                log.info('|{}| |Slack| Retrieved the following message from user [{}] in channel [{}]: [{}]'
                         .format(count.get_count(), user, channel, text))
                return text, channel
        return None, None

    def send_message(self, message, channel):
        """
        Send message
        :param message: text to send
        :param channel: channel where send
        :return: message sent
        """
        log.info('|{}| |Slack| Sent the following message in channel [{}]: [{}]'
                 .format(count.get_count(), channel, message))
        count.update_count()
        return self.client.api_call(
            SLACK_API_METHOD,
            channel=channel,
            text=message
        )

    def notify(self, message, channel=SLACK_API_CHANNEL):
        """
        Notify a message to an specific channel
        :param message: message
        :param channel: channel
        :return: message notified
        """
        return self.client.api_call(
            SLACK_API_METHOD,
            channel=channel,
            text=message
        )

# noinspection PyPackageRequirements
import slack
import multiprocessing.dummy as mp

from hackupc.bienebot import *
from hackupc.bienebot.luis import luis
from hackupc.bienebot.util import log


class Slack:

    def __init__(self):
        self.web_client = slack.WebClient(token=SLACK_API_CHANNEL, timeout=30)
        self.rtm_client = slack.RTMClient(token=SLACK_API_TOKEN, timeout=30)

    def rtm_start(self):
        """
        Connects to the RTM web socket.
        :return: True if it's connected successfully, False otherwise.
        """
        return self.rtm_client.start()

    def worker(self, message, channel, user):
        """
        Worker for interpreting the message from Slack.
        :param message: Message.
        :param channel: Channel.
        :param user: User.
        :return: Response sent.
        """
        # Biene in Random
        if channel == SLACK_API_RANDOM:
            if 'biene' in message.lower():
                self.send_message('BIENE', channel)
        # Luis interaction
        else:
            response, intent, score = luis.get_intent(message)
            for mess in response:
                self.send_message(mess, channel)
                log.save_activity(user, channel, intent, score, message, mess)

    def send_message(self, message, channel=SLACK_API_CHANNEL):
        """
        Send message.
        :param message: Text to send.
        :param channel: Channel where send.
        :return: Message sent.
        """
        log.info('|Slack| Sent the following message in channel [{}]: [{}]'.format(channel, message.replace('\n', '')))
        return self.web_client.chat_postMessage(channel=channel, text=message)

    @slack.RTMClient.run_on(event='message')
    def answer(self, **payload):
        """
        Retrieve messages.
        :return: Thread run.
        """
        if 'ts' not in payload:
            text = payload['text']
            channel = payload['channel']
            user = payload['user']
            log.info('|Slack| Retrieved the following message from user [{}] in channel [{}]: [{}]'.format(
                user, channel, text.replace('\n', ''))
            )
            process = mp.Process(target=self.worker, args=(text, channel, user))
            process.daemon = True
            process.start()

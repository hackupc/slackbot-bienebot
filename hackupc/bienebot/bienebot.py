from hackupc.bienebot.slack.slack import Slack
from hackupc.bienebot.util import log


def run():
    """
    Run Biene Bot.
    :return: Biene bot ran
    """
    slack = Slack()
    try:
        slack.rtm_start()
    except Exception as e:
        log.error(e, slack)
    finally:
        log.info('|BIENE| Biene Bot stopped!')
        slack.send_message(':bee: Biene Bot stopped!')
        return

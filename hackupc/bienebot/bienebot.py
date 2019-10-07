from hackupc.bienebot.slack import slack
from hackupc.bienebot.util import log


def run():
    """
    Run Biene Bot.
    :return: Biene bot ran
    """
    rtm_client = slack.get_rtm_client()
    try:
        slack.send_message(':bee: Biene Bot starting!')
        rtm_client.start()
    except Exception as e:
        log.exception(e)
        log.error(e, notify=True)
    finally:
        log.info('|BIENE| Biene Bot stopped!')
        slack.send_message(':bee: Biene Bot stopped!')
        return

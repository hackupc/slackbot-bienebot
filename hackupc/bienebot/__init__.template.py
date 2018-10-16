"""
Global vars for bienebot module
"""

# Slack API
SLACK_API_TOKEN = ''  # token for bienebot
SLACK_API_METHOD = 'chat.postMessage'
SLACK_API_CHANNEL = ''
SLACK_API_RANDOM = ''

# Luis stuff
LUIS_SUBSCRIPTION_KEY = ''
LUIS_SERVER = ''
LUIS_ID = ''

# Bot stuff
RTM_READ_DELAY = 1  # 1 second delay between reading from RTM
SCORE_THRESHOLD = 0.5  # for avoiding wrong answers

__all__ = [
    'SLACK_API_TOKEN',
    'SLACK_API_METHOD',
    'SLACK_API_CHANNEL',
    'SLACK_API_RANDOM',
    'LUIS_SUBSCRIPTION_KEY',
    'LUIS_SERVER',
    'LUIS_ID',
    'RTM_READ_DELAY',
    'SCORE_THRESHOLD'
]

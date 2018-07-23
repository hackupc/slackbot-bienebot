"""
Global vars for bienebot module
"""

# Slack API
SLACK_API_TOKEN = ''  # token for bienebot
SLACK_API_METHOD = 'chat.postMessage'

# Luis stuff
LUIS_SUBSCRIPTION_KEY = ''
LUIS_SERVER = ''
LUIS_ID = ''

# Bot stuff
RTM_READ_DELAY = 1  # 1 second delay between reading from RTM

__all__ = [
    'SLACK_API_TOKEN',
    'SLACK_API_METHOD',
    'LUIS_SUBSCRIPTION_KEY',
    'LUIS_SERVER',
    'LUIS_ID',
    'RTM_READ_DELAY'
]

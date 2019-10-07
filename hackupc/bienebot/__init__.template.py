# Slack API
SLACK_API_TOKEN = ''  # Token for Biene bot
SLACK_API_METHOD = 'chat.postMessage'
SLACK_API_CHANNEL = ''
SLACK_API_RANDOM = ''

# Luis stuff
LUIS_SUBSCRIPTION_KEY = ''
LUIS_SERVER = ''
LUIS_ID = ''

# Bot stuff
RTM_READ_DELAY = 0.05  # 0.05 second delay between reading from RTM
SCORE_THRESHOLD = 0.5  # For avoiding wrong answers

# Other stuff
SCHEDULE_JSON_URL = 'https://raw.githubusercontent.com/hackupc/frontend/master/src/data/schedule.json'


__all__ = [
    'SLACK_API_TOKEN',
    'SLACK_API_METHOD',
    'SLACK_API_CHANNEL',
    'SLACK_API_RANDOM',
    'LUIS_SUBSCRIPTION_KEY',
    'LUIS_SERVER',
    'LUIS_ID',
    'RTM_READ_DELAY',
    'SCORE_THRESHOLD',
    'SCHEDULE_JSON_URL'
]

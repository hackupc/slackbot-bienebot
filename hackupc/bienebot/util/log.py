import datetime
import logging
import os
import sys

from hackupc.bienebot.slack import slack


# Setup main loggers
__logger_stdout = logging.getLogger('hackupc_bienebot')

# Setup formatter
__formatter = logging.Formatter('{%(name)s} - <%(asctime)s> - [%(levelname)-7s] - %(message)s')

# Setup stdout stream handler
__handler_stdout = logging.StreamHandler(sys.stdout)
__handler_stdout.setFormatter(__formatter)
__logger_stdout.addHandler(__handler_stdout)
__logger_stdout.setLevel(logging.INFO)


def debug(msg):
    """
    Optimized debugging log call which wraps with debug check to prevent unnecessary string creation.
    :param msg: Message to debug.
    :return: Message debugged.
    """
    if __logger_stdout.isEnabledFor(logging.DEBUG):
        __logger_stdout.debug(msg)


def info(msg):
    """
    Log [INFO] level log messages.
    :param msg: Message to log.
    :return: Message logged.
    """
    __logger_stdout.info(msg)


def warn(msg):
    """
    Log [WARNING] level log messages.
    :param msg: Message to log.
    :return: Message logged.
    """
    __logger_stdout.warning(msg)


def error(msg, notify=False):
    """
    Log [ERROR] level log messages.
    :param msg: Message to log.
    :param notify: True if the message has to be notified through Slack, False otherwise.
    :return: Message logged.
    """
    __logger_stdout.error(msg)
    if notify:
        slack.send_message(f':warning: ERROR: {msg}')


def exception(msg):
    """
    Log [EXCEPTION] level log messages.
    :param msg: Message to log.
    :return: Message logged.
    """
    __logger_stdout.exception(msg)


def save_activity(user, channel, intent, score, message, response):
    """
    Save activity in CSV files.
    :param user: User which is interacting with the bot.
    :param channel: Channel between user and bot.
    :param intent: LUIS intent.
    :param score: LUIS score.
    :param message: User message.
    :param response: Bot message.
    :return: New row was added in a CSV file.
    """
    string_date = datetime.datetime.now().strftime('%Y-%m-%d')
    file_name = f'logs/log_biene_bot_{string_date}.csv'
    exists = os.path.isfile(file_name)
    with open(file_name, 'a') as file:
        if not exists:
            file.write('"{}","{}","{}","{}","{}","{}","{}"\n'.format(
                'DATE', 'USER', 'CHANNEL', 'INTENT', 'SCORE', 'MESSAGE', 'RESPONSE'
            ))
        row = '"{}","{}","{}","{}","{}","{}","{}"\n'.format(
            datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            user,
            channel,
            intent,
            score,
            message.replace('\n', ''),
            response.replace('\n', '')
        )
        file.write(row)

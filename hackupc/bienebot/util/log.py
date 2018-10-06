"""
Logging utility for more robust logging
"""
import datetime
import logging
import os

# setup main loggers
__logger_stdout = logging.getLogger('hackupc_bienebot')

# setup formatter
__formatter = logging.Formatter('{%(name)s} - <%(asctime)s> - [%(levelname)-7s] - %(message)s')

# setup stdout stream handler
__logger_stdout.setLevel(logging.INFO)


def debug(msg):
    """
    Optimized debugging log call which wraps with debug check to prevent unnecessary string creation
    """
    if __logger_stdout.isEnabledFor(logging.DEBUG):
        __logger_stdout.debug(msg)


def info(msg):
    """
    Log [INFO] level log messages
    """
    __logger_stdout.info(msg)


def warn(msg):
    """
    Log [WARNING] level log messages
    """
    __logger_stdout.warning(msg)


def error(msg):
    """
    Log [ERROR] level log messages
    """
    __logger_stdout.error(msg)


def exception(msg):
    """
    Log [ERROR] level log messages
    """
    __logger_stdout.exception(msg)


def save_activity(user, channel, intent, score, message, response):
    """
    Save activity in csv files
    :param user: user which is interacting with the bot
    :param channel: channel between user and bot
    :param intent: luis intent
    :param score: luis score
    :param message: user message
    :param response: bot message
    :return: new row was added in a csv file
    """
    file_name = 'logs/log_biene_bot_{date}.csv'.format(date=datetime.datetime.now().strftime("%Y-%m-%d"))
    exists = os.path.isfile(file_name)
    with open(file_name, 'a') as file:
        if not exists:
            file.write('"{}","{}","{}","{}","{}","{}","{}"\n'
                       .format('DATE', 'USER', 'CHANNEL', 'INTENT', 'SCORE', 'MESSAGE', 'RESPONSE'))
        row = '"{}","{}","{}","{}","{}","{}","{}"\n'.format(
            datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            user,
            channel,
            intent,
            score,
            message.replace('\n', ''),
            response.replace('\n', '')
        )
        file.write(row)

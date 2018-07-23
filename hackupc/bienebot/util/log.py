"""
Logging utility for more robust logging
"""
import logging
import sys


# setup main loggers
__logger_stdout = logging.getLogger('hackupc_bienebot')

# setup formatter
__formatter = logging.Formatter('{%(name)s} - <%(asctime)s> - [%(levelname)-7s] - %(message)s')

# setup stdout stream handler
__handler_stdout = logging.StreamHandler(sys.stdout)
__handler_stdout.setFormatter(__formatter)
__logger_stdout.addHandler(__handler_stdout)
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

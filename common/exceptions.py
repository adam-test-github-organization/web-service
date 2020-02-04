import logging
logger = logging.getLogger(__name__)


class InvalidResponseException(Exception):
    def __init__(self, message):
        logger.error(f'Error: A non 200 response received with message: {message}')
        Exception.__init__(self, f'Error: A non 200 response received with message: {message}')

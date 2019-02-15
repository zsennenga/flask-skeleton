import logging

from config.config import Config

_logger = None


class LoggingService:
    @property
    def logger(self):
        global _logger

        if _logger is None:
            _logger = logging.getLogger(Config.app_name)

        return _logger


logging_service = LoggingService()

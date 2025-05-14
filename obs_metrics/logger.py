from datetime import datetime
from .config import config
from .logs_sink import send_log

class Logger:
    def __init__(self, service_name=None):
        self.service_name = service_name or config.SERVICE_NAME
        self.environment = config.ENVIRONMENT

    def _build_log(self, level, message, context=None):
        return {
            "timestamp": str(datetime.now()),
            "level": level.upper(),
            "service": self.service_name,
            "environment": self.environment,
            "message": message,
            "context": context or {}
        }

    def info(self, message, context=None):
        log = self._build_log("info", message, context)
        send_log(log)

    def error(self, message, context=None):
        log = self._build_log("error", message, context)
        send_log(log)

    def debug(self, message, context=None):
        log = self._build_log("debug", message, context)
        send_log(log)

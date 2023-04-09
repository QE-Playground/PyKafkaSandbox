import sys
import logging

from src.libs.Singleton import Singleton


class Logger(object, metaclass=Singleton):
    _log: any

    @property
    def log(self):
        return self._log

    def __init__(self):
        self._log = logging.getLogger('')
        self._log.setLevel(logging.INFO)
        format_logging = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

        ch = logging.StreamHandler(sys.stdout)
        ch.setFormatter(format_logging)
        self._log.addHandler(ch)

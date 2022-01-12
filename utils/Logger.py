import sys
import logging


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


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
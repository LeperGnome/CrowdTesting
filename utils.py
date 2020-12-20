from environs import Env
import functools
from loguru import logger


logger.add(
    'debug.log',
    format="{time} {level} {message}",
    level='DEBUG',
    rotation='1 MB',
    compression="zip",
    backtrace=True,
    diagnose=True,
    colorize=True,
)

env = Env()
env.read_env('.env')


class ServerError(Exception):
    def __init__(self, message='Server error', status=500, *args, **kwargs):
        self.message = message
        self.status = status
        super().__init__()


def error_hadler(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except Exception as ex:
            message = getattr(ex, 'message', 'Server error')
            status = getattr(ex, 'status', 500)
            logger.exception(f"Route error: {message, status}")
            res = {'message': message}, status
        finally:
            return res

    return inner

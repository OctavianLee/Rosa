"""
Basic Decorators Suites.
"""
# -*- coding: utf-8 -*-
import time
from pytest import raises


class TimeExpired(AssertionError):

    """An Exception about Time out."""
    pass


def rais(*exceptions):
    """A decorator about raises.

    It will raise exceptions that the function captured.

    :param exceptions: exceptions it will raise.
    """
    def deco(func):
        """Decorator"""
        def newfunc(*args, **kwargs):
            """Function executes."""
            raises(exceptions, func(*args, **kwargs))
        return newfunc
    return deco


def timed(limit):
    """A decorator about function timeout.

    It will raise TimeExpired when timeout.

    :param limit: the timeout value.
    """
    def deco(func):
        """Decorator"""
        def newfunc(*args, **kwargs):
            """Function executes."""
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            if end - start > limit:
                raise TimeExpired('Time limit: {} exceeded'.format(limit))
            return result
        return newfunc
    return deco

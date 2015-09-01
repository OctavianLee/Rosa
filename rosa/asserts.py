"""
Basic Assert Suites.
"""
# -*- coding: utf-8 -*-


def eq_(left, right, msg=None):
    """Assert two elements are equal.

    :param left: the left element in the assert.
    :param right: the right element in the assert.
    :param msg: the message of assert.

    :except: AssertionError.
    """

    assert left == right, msg


def neq_(left, right, msg=None):
    """Assert two elements are not equal.

    :param left: the left element in the assert.
    :param right: the right element in the assert.
    :param msg: the message of assert.

    :except: AssertionError.
    """

    assert left != right, msg


def in_(left, right, msg=None):
    """Assert the left element is in the right.

    :param left: the left element in the assert.
    :param right: the right element in the assert.
    :param msg: the message of assert.

    :except: AssertionError.
    """

    assert left in right, msg


def nin_(left, right, msg=None):
    """Assert the left element is not in the right.

    :param left: the left element in the assert.
    :param right: the right element in the assert.
    :param msg: the message of assert.

    :except: AssertionError.
    """

    assert left not in right, msg


def is_ins(left, right, msg=None):
    """Assert the left element is an instance of the right.

    :param left: the left element in the assert.
    :param right: the right element in the assert.
    :param msg: the message of assert.

    :except: AssertionError.
    """

    assert isinstance(left, right), msg


def eq_obj(left, right, msg=None):
    """Assert the value of the left object is equal to the right.

    :param left: the left element in the assert.
    :param right: the right element in the assert.
    :param msg: the message of assert.

    :except: AssertionError.
    """

    assert left.__dict__ == right.__dict__, msg

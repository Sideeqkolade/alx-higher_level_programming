#!/usr/bin/python3
"""Defines the addition of two integers"""


def add_integer(a, b=98):
    """Returns the addition of a and b

    a and b must be casted into integer if they are of float type

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.

    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    elif ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))

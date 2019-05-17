#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Assignment 14 - Recursion"""


def fibonnaci(n):
    """The fibonnaci sequence. Returns the nth element.

    Args:
        n (int): The element to run the sequence to.

    Returns:
        int: The nth element in the Fibonnaci Sequence.
    """
    if n == 0 or n == 1:
        return -1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


print fibonnaci(12)


def gcd(a, b):
    """Returns the greatest common divisor.

    Returns:
        int: The greatest common divisor shared. 
    """
    return gcd(b, a % b) if b else abs(a)


# Should equal 2
print gcd(10, 4)


def compareTo(s1, s2):
    """Compares two strings and returns an output.

    Args:
        s1 (string): A string to compare.
        s2 (string): A string to compare.

    Returns:
        int: 0 if equal length.
        int: 1 if the first string is longer.
        int: -1 if the second string is longer.
    """
    if not s1 and not s2:
        return 0
    elif not s1:
        return -1
    elif not s2:
        return 1
    else:
        return compareTo(s1[1:], s2[1:])


print compareTo('pepper', 'salt')
print compareTo('ketchup', 'ketchup')
print compareTo('hambuger', 'frenchfries')

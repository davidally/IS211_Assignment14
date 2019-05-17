#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Assignment 14 - Recursion"""


def fibonnaci(n):
    if n == 0 or n == 1:
        return -1
    else:
        return fibonnaci(n - 1) + fibonnaci(n - 2)


print fibonnaci(12)


def gcd(a, b):
    return gcd(b, a % b) if b else abs(a)


# Should equal 2
print gcd(10, 4)


def compareTo(s1, s2):
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

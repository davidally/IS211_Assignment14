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


print gcd(10, 4)

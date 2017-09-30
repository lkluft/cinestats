# -*- coding: utf-8 -*-
"""Provide datastructures to handel single movies as well as databases.
"""
__all__ = [
    'Movie',
]


class Movie:
    def __init__(self, title, date=None):
        self.title = title
        self.date = date

    def __repr__(self):
        return self.title

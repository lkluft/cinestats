# -*- coding: utf-8 -*-
"""Provide datastructures to handel single movies as well as databases.
"""
from matplotlib.dates import datestr2num
import numpy as np


__all__ = [
    'Movie',
    'MovieDatabase',
]


class Movie:
    def __init__(self, title, date=None):
        self.title = title
        self.date = date

    def __repr__(self):
        return "'{title}'".format(title=self.title)

    def __lt__(self, other):
        return self.datenum < other.datenum

    def __eq__(self, other):
        return self.datenum < other.datenum

    @property
    def datenum(self):
        """Return datenum representation of date."""
        return datestr2num(self.date) if self.date is not None else None


class MovieDatabase(list):
    @classmethod
    def from__csv(cls, filename):
        """Load a movie database from CSV file.

        Parameters:
            filename (str): Path to CSV file.
        """
        # Read the full CSV file into a structured ndarray.
        database_array = np.genfromtxt(
            fname=filename,
            delimiter=',',
            names=True,  # expect field names in first row.
            dtype=None,  # automatically determine dtype of fields.
        )

        # Create Movie object from every row in the array (line in CSV).
        movie_list = [Movie(title.decode(), date.decode()) for title, date
                      in zip(database_array['movie'], database_array['date'])]

        # Return actual MovieDatabase.
        return cls(movie_list)

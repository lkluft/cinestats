# -*- coding: utf-8 -*-
"""Provide datastructures to handel single movies as well as databases.
"""
import csv
from operator import itemgetter

import matplotlib.pyplot as plt
from matplotlib.dates import (DateFormatter, datestr2num)


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

        Note:
            If the movie title contains a comma, the title has to be quoted:
                2016-02-05,"Hail, Caesar!"

        Parameters:
            filename (str): Path to CSV file.
        """
        with open(filename, 'r') as csvfile:
            # Parse the CSV file into a dictionary (column names as keys).
            reader = csv.DictReader(csvfile)
            # Create Movie object from every entry in the CSV reader.
            movie_list = [Movie(title=line['movie'], date=line['date'])
                          for line in reader]

        # Return actual MovieDatabase.
        return cls(movie_list)

    def get_datenumlim(self):
        """Return the start and end date of the database as datenum.

        Returns:
            float, float: Start date, end date
        """
        # Get the first and last movie of the list sorted by date.
        firstlast = itemgetter(0, -1)(sorted(self))

        # Return the datenum representation of both movies.
        return map(lambda m: m.datenum, firstlast)

    def plot_titles(self, ax=None, **kwargs):
        """Plot number of movies seen against date.

        Parameters:
            ax (plt.AxesSubplot): Axes to plot in.
            **kwargs: Additional keyword arguments are collected
                and passed to `plt.annotate`.
        """
        # If no matplotlib axes is passed, get the latest.
        if ax is None:
            ax = plt.gca()

        # Loop over all movies in the sorted database and ...
        for n, movie in enumerate(sorted(self), 1):
            # ... print their title against their position in the database.
            ax.annotate(' ' + movie.title, xy=(movie.datenum, n), **kwargs)

        # Date formatting for the x-axis.
        ax.xaxis.set_major_formatter(DateFormatter("%b"))

        # Axes limits have to be set as `plt.annotate` does not to this!
        ax.set_xlim(self.get_datenumlim())
        ax.set_ylim(bottom=0, top=n + 1)

        ax.set_ylabel('Absolute frequency')
        ax.grid(True)

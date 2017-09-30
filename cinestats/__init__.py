"""Analyse and visualise statistics around movies and cinema.
"""
from os.path import (dirname, join)


# Parse version number from module-level ASCII file.
__version__ = open(join(dirname(__file__), 'VERSION')).read().strip()

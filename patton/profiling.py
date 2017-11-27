"""
Module to allow profiling to a file within a context manager
"""

import cProfile
from contextlib import contextmanager


@contextmanager
def profile_ctx(profile_path=''):
    """
    Wrapper around to isolate responsability of profiling in a contextmanager
    """

    if profile_path is not '':
        pr = cProfile.Profile()
        pr.enable()

    yield

    if profile_path is not '':
        pr.disable()
        pr.dump_stats(profile_path)

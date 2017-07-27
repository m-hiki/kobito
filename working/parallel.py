# coding: utf-8
import logging
import time
import working


DEFAULT_LINE = 2


class Parallel(object):
    """Parallel
    """

    def __init__(self, stage=2, works=[]):
        self.workers = []

    def request(self, work):
        self.workers[0].request(work)
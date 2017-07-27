# -*- coding: utf-8 -*-
import logging
import time
from work.worker import Worker


class Pipeline(object):
    """Pipeline"""

    def __init__(self, step=2):
        self.log = logging.getLogger(__name__)
        self.start_time = time.time()

        if step < 2:
            step = 2

        self.workers = []
        prev_worker = None
        for _ in range(step):
            self.workers.append(Worker(num_thread=1, follower=prev_worker))
            prev_worker = self.workers[-1]

        self.log.info('pipeline start')


    def request(self, work):
        """request"""


    def stop(self):
        """stop"""
        elapsed_time = time.time() - self.start_time
        self.log.info('pipeline stop: {0}'.format(elapsed_time) + '[sec]')

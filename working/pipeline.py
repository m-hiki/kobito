# -*- coding: utf-8 -*-
import logging
import time
import working


DEFAULT_STAGE = 2


class Pipeline(object):
    """Pipeline"""

    def __init__(self, stage=2, works=[]):
        self.log = logging.getLogger(__name__)
        self.start_time = time.time()
        self.stage = stage if stage < DEFAULT_STAGE else DEFAULT_STAGE
        self.workers = []
        prev_worker = None
        for i in range(stage):
            worker = working.Worker(work_name=works[i], follower=prev_worker)
            self.workers.append(worker)
            prev_worker = self.workers[-1]

        self.log.info('pipeline start')

    def set_work_name(self, no, work_name):
        #self.workers[no]
        pass

    def request(self, work):
        """request"""
        self.workers[0].request(work)

    def stop(self):
        """stop"""
        for worker in self.workers:
            worker.stop()

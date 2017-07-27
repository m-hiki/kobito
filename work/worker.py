# -*- coding: utf-8 -*-
import logging
try:
    import Queue as queue
except ImportError:
    import queue
import time
import threading


DEFAULT_NUM_THREAD = 4
MAX_QUEUE_SIZE = 2000


class Worker(object):
    """Workers is the multithread task executer with queue."""


    def __init__(self, num_thread=DEFAULT_NUM_THREAD, follower=None):
        self.log = logging.getLogger(__name__)
        self._num_thread = num_thread
        self._queue = queue.Queue(maxsize=MAX_QUEUE_SIZE)
        self._threads = []
        self.__create_worker_thread()
        self._follower = follower
        self.start_time = time.time()
        self.log.info('Worker start')


    def __del__(self):
        if self._threads is not None:
            self.stop()


    def __create_worker_thread(self):
        for thread in range(self._num_thread):
            thread = threading.Thread(target=self.__do_work)
            #thread.setDaemon(True)
            thread.start()
            self._threads.append(thread)


    def __do_work(self):
        self.log.info('Thread start')
        while True:
            work = self._queue.get()
            if work is None:
                break
            self.log.info('Work start')
            getattr(work, 'run')()
            self.log.info('Work finish')
            if self._follower is not None:
                self._follower.request(work)
            self._queue.task_done()
        self.log.info('Thread finish')


    def request(self, work):
        """request"""
        self._queue.put(work)


    def stop(self):
        """stop"""

        self._queue.join()

        for _ in range(self._num_thread):
            self._queue.put(None)
        for thread in self._threads:
            thread.join()

        self._threads = None
        elapsed_time = time.time() - self.start_time
        self.log.info('Worker stop: {0}'.format(elapsed_time) + '[sec]')

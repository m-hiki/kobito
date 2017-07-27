# -*- coding: utf-8 -*-
"""

"""
import logging
try:
    import Queue as queue
except ImportError:
    import queue
import time
import threading


MAX_QUEUE_SIZE = 2000


class Worker(object):
    """Workers is a task executer with a queue."""


    def __init__(self, work_name='run', follower=None):
        self.logger = logging.getLogger(__name__)
        self._work_name = work_name
        self._queue = queue.Queue(maxsize=MAX_QUEUE_SIZE)
        self._thread = threading.Thread(target=self.__do_work)
        #thread.setDaemon(True)
        self._thread.start()
        self._follower = follower


    def __del__(self):
        if self._thread is not None:
            self.stop()


    def __do_work(self):
        self.__log('worker thread start')
        while True:
            work = self._queue.get()
            if work is None:
                break
            self.__log('work start')
            start_time = time.time()
            getattr(work, self._work_name)()
            elapsed_time = time.time() - start_time
            self.__log('work finish: {0}'.format(elapsed_time) + '[sec.]')
            self._queue.task_done()
            if self._follower is not None:
                self._follower.request(work)
        self.__log('worker thread stop')


    def request(self, work):
        """request"""
        self._queue.put(work)


    def stop(self):
        """stop"""
        self._queue.join()
        self._queue.put(None)
        self._thread.join()
        self._thread = None


    def __log(self, message):
        logger = logging.getLogger(__name__)
        logger.info(self._work_name + ' ' + message)
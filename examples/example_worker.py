# -*- coding: utf-8 -*

from __future__ import print_function
import logging
import working

LOG_FORMAT = '%(asctime)s [%(levelname)s] (%(threadName)-10s) %(message)s'

class Example(object):
    """Example"""
    def __init__(self, name):
        self.name = name

    def hello(self):
        """task"""
        print('Hello, ' + self.name + '!')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

    worker = working.Worker(work_name='hello')

    worker.request(Example('Hiro'))
    worker.request(Example('Tadashi'))
    worker.request(Example('Mika'))
    #worker.request(type('', (), {'hello': lambda self: print('Hello, Kaori!')}))
    
    worker.stop()

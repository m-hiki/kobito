# -*- coding: utf-8 -*

import unittest
import working


class TestWorker(unittest.TestCase):
    """ Worker unit test stubs """
    def setUp(self):
        self.worker = working.Worker()
    
    def teaDown(self):
        pass
    
    def test_request(self):
        pass

    def test_stop(self):
        pass

if __name__ == '__main__':
    unittest.main()
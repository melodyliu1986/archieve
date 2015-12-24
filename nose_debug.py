__author__ = 'liusong'

import os
import logging
import logging.config
import unittest

log_config_file = "{0}/logging.conf".format(os.getcwd())
logger = logging.getLogger(__name__)


class ADD(unittest.TestCase):

    def setUp(self):
        self.file_name = "{0}/nose_debug.log".format(os.getcwd())
        logging.config.fileConfig(log_config_file, defaults={"logfilename":self.file_name})

    def test_add(self):
        logging.info("Test add function!")
        print "Test add function"
        self.assertEqual(1+1, 2, 'Failed to validate the add function!')

    def test_multiply(self):
        logging.info("Test multiply function!")
        self.assertTrue(4*4==15, 'Failed to validate the multiply function!')


__author__ = 'liusong'

import os
import logging
import logging.config
import unittest


class ADD(unittest.TestCase):

    def setUp(self):
        log_config_file_path = "{0}/logging.conf".format(os.getcwd())
        logging_file_name = "{0}/test.log".format(os.getcwd())
        logging.config.fileConfig(log_config_file_path, defaults={'logfilename': logging_file_name})
        self.logger = logging.getLogger("skuValidation")

    def test_add(self):
        self.logger.info("Test add function!")
        self.assertEqual(1+1, 2, 'Failed to validate the add function!')

    def test_multiply(self):
        self.logger.info("Test multiply function!")
        self.assertTrue(4*4==15, 'Failed to validate the multiply function!')


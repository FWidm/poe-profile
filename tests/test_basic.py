# -*- coding: utf-8 -*-
import logging

import sys

from src.core import PoeData

import unittest


class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_get_chars(self):
        pp = PoeData()
        result = pp.get_char_list('FaustVIII')
        self.assertNotEqual(result, None)
        self.assertIsInstance(result, list)


    def test_get_char_items(self):
        pp = PoeData()
        result = pp.get_char_info('FaustVIII','fromdeadtoworse')
        self.assertNotEqual(result, None)
        self.assertIsInstance(result, dict)

if __name__ == '__main__':
    logger = logging.getLogger()
    logger.level = logging.DEBUG
    stream_handler = logging.StreamHandler(sys.stdout)
    logger.addHandler(stream_handler)
    unittest.main()

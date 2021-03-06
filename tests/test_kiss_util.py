#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for KISS Util Module."""

__author__ = 'Greg Albrecht W2GMD <oss@undef.net>'
__copyright__ = 'Copyright 2016 Orion Labs, Inc. and Contributors'
__license__ = 'Apache License, Version 2.0'


import logging
import unittest

from .context import kiss

from . import constants


# pylint: disable=R0904,C0103
class KISSUtilTestCase(unittest.TestCase):

    """Test class for KISS Python Module."""

    _logger = logging.getLogger(__name__)
    if not _logger.handlers:
        _logger.setLevel(kiss.LOG_LEVEL)
        _console_handler = logging.StreamHandler()
        _console_handler.setLevel(kiss.LOG_LEVEL)
        _console_handler.setFormatter(kiss.LOG_FORMAT)
        _logger.addHandler(_console_handler)
        _logger.propagate = False

    def setUp(self):
        """Setup."""
        self.test_frames = open(constants.TEST_FRAMES, 'r')
        self.test_frame = self.test_frames.readlines()[0].strip()

    def tearDown(self):
        """Teardown."""
        self.test_frames.close()

    def test_escape_special_codes_fend(self):
        """
        Tests `kiss.escape_special_codes` util function.
        """
        fend = kiss.escape_special_codes(kiss.FEND)
        self._logger.debug('fend=%s', fend)
        self.assertEqual(fend, kiss.FESC_TFEND)

    def test_escape_special_codes_fesc(self):
        """
        Tests `kiss.escape_special_codes` util function.
        """
        fesc = kiss.escape_special_codes(kiss.FESC)
        self._logger.debug('fesc=%s', fesc)
        self.assertEqual(fesc, kiss.FESC_TFESC)

    def test_extract_ui(self):
        """
        Tests `kiss.extract_ui` util function.
        """
        frame_ui = kiss.extract_ui(self.test_frame)
        self._logger.debug('frame_ui=%s', frame_ui)
        self.assertEqual('APRX240W2GMD 6WIDE1 1', frame_ui)


if __name__ == '__main__':
    unittest.main()

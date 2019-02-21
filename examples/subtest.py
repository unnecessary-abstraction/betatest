# Copyright (c) 2019 Beta Five Ltd
#
# SPDX-License-Identifier: Apache-2.0
#

"""Example code using the subtest decorator."""

import os
import sys
import unittest

# Expect to find betatest in the working directory when running these examples
# pylint: disable=wrong-import-position
sys.path.insert(0, os.getcwd())
from betatest.amtest import AMTestRunner
from betatest.subtest import subtest

class TestPasses(unittest.TestCase):
    @subtest
    def phase_1(self):
        self.assertEqual(1, 1)

    @subtest
    def phase_2(self, color):
        self.assertIsNotNone(color)

    def test_all(self):
        self.phase_1()
        self.phase_2(color='red')
        self.phase_2(color='green')

class TestFails(unittest.TestCase):
    @subtest
    def phase_1(self):
        self.assertEqual(1, 0)

    @subtest
    def phase_2(self):
        self.assertEqual(2, 2)

    @subtest
    def phase_3(self, color):
        self.assertEqual(color, 'red')

    def test_all(self):
        self.phase_1()
        self.phase_2()
        self.phase_3(color='red')
        self.phase_3(color='green')

# Allow a '--pass' argument to disable tests that will fail. This is useful for
# running the example in CI.
if len(sys.argv) > 1 and sys.argv[1] == '--pass':
    del TestFails
    del sys.argv[1]

if __name__ == '__main__':
    unittest.main(testRunner=AMTestRunner)

# Copyright (c) 2018-2019 Beta Five Ltd
#
# SPDX-License-Identifier: Apache-2.0
#

"""Example code using the AMTestRunner class."""

import os
import sys
import unittest

# Expect to find betatest in the working directory when running these examples
# pylint: disable=wrong-import-position
sys.path.insert(0, os.getcwd())
from betatest.amtest import AMTestRunner

class TestPasses(unittest.TestCase):
    def test_pass(self):
        pass

    @unittest.skip('Skipped')
    def test_skip(self):
        pass

    @unittest.expectedFailure
    def test_xfail(self):
        self.fail('Expected failure')

class TestFails(unittest.TestCase):
    def test_fail(self):
        self.fail('Unexpected failure')

    @unittest.expectedFailure
    def test_xpass(self):
        pass

    def test_error(self):
        self.assertEqual(1.0/0, 1)

# Allow a '--pass' argument to disable tests that will fail. This is useful for
# running the example in CI.
if len(sys.argv) > 1 and sys.argv[1] == '--pass':
    del TestFails
    del sys.argv[1]

if __name__ == '__main__':
    unittest.main(testRunner=AMTestRunner)

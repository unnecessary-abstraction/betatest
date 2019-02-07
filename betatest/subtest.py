#
# Subtest decorator.
#
# Copyright (c) 2019 Beta Five Ltd
#
# SPDX-License-Identifier: Apache-2.0
#

import functools

def subtest(testfn, msg=None):
    """Mark a helper function within a TestCase class as a subtest"""
    if not msg:
        msg = testfn.__name__

    @functools.wraps(testfn)
    def wrapper(self, *args, **kwargs):
        with self.subTest(msg, **kwargs):
            testfn(self, *args, **kwargs)

    return wrapper

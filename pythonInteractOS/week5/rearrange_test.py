#!/usr/bin/env python3

# import the function (part of program) you want to test
from rearrange import rearrange_name
# this module contains methods for testing
import unittest

class TestRearrange(unittest.TestCase):
    """ This class inherits the test case methods from
        unittest.TestCase class. Any method that starts
        with test (a convention) is a test case. """
    def test_basic(self):
        testcase = "Lovelace, Ada"
        expected = "Ada Lovelace"
        # Check if the expected result is meet
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_one_name(self):
        testcase = "Voltaire"
        expected = "Voltaire"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()

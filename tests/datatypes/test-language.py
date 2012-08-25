# -*- coding: utf-8 -*-
from pyxb.exceptions_ import *
import unittest
import pyxb.binding.datatypes as xsd

class Test_language (unittest.TestCase):
    def testValid (self):
        valid = [ 'english', 'welsh', 'french-english', 'one-two-three-four' ]
        for f in valid:
            self.assertEqual(f, xsd.language(f))

    def testInvalid (self):
        invalid = [ 'toomanychars', 'illegal_chars', 'numb3rs' ]
        for f in invalid:
            self.assertRaises(BadTypeValueError, xsd.language, f)

if __name__ == '__main__':
    unittest.main()

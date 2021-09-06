import unittest
from arithmetic import *
class Test_arithmetic(unittest.TestCase):
    def setUp(self):
        self.a = arithmetic()
    def test_add(self):
        self.assertEqual(5, self.a.add(2,3))
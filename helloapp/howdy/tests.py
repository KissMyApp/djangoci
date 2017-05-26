import unittest
from howdy.apps import Math
from django.test import TestCase

# Create your tests here.
class MathTest(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(Math.addition(3,4),8)

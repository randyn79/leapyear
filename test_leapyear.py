#!/usr/bin/env python3

import unittest
import leapyear

class TestLeapYear(unittest.TestCase):

    def test_leapyear(self):
        """Tests the leapyear.leapyear function."""
        # If year is not an integer
        self.assertRaises(TypeError, leapyear.leapyear, 2.3)
        self.assertRaises(TypeError, leapyear.leapyear, 'hello')

        # If year is lower than one:
        self.assertRaises(ValueError, leapyear.leapyear, -1)
        self.assertRaises(ValueError, leapyear.leapyear, 0)

        # If year is evenly divisible by 100:
        
        # True - if year is also evenly divisible by 400
        self.assertTrue(leapyear.leapyear(2000))
        
        # False - if year is not also evenly divisible by 400
        self.assertFalse(leapyear.leapyear(1900))
        
        # If year is not divisible by 100:

        # True - if year is evenly divisible by 4
        self.assertTrue(leapyear.leapyear(1904))

        # False - if year is not evenly divisible by 4
        self.assertFalse(leapyear.leapyear(1905))

        # Return is bool
        self.assertIsInstance(leapyear.leapyear(1904), bool)
        self.assertIsInstance(leapyear.leapyear(1905), bool)

    def test_leapyear_range(self):
        """Tests the leapyear.leapyear_range function."""
        # If first, last are not integers
        self.assertRaises(TypeError, leapyear.leapyear_range,2.3,3.5)
        self.assertRaises(TypeError, leapyear.leapyear_range,4.8,3.2)
        self.assertRaises(TypeError, leapyear.leapyear_range,1.75,2000)
        self.assertRaises(TypeError, leapyear.leapyear_range,1900,2001.5)

        # If first, last are lower than one
        self.assertRaises(ValueError, leapyear.leapyear_range, -1, -10)
        self.assertRaises(ValueError, leapyear.leapyear_range, -10, -1)
        self.assertRaises(ValueError, leapyear.leapyear_range, 10, -10)
        self.assertRaises(ValueError, leapyear.leapyear_range, -10, 10)
        self.assertRaises(ValueError, leapyear.leapyear_range, 0, 10)
        self.assertRaises(ValueError, leapyear.leapyear_range, 10, 0)
        self.assertRaises(ValueError, leapyear.leapyear_range, 0, -10)
        self.assertRaises(ValueError, leapyear.leapyear_range, -10, 0)

        # Returns list of correct values
        self.assertEqual(leapyear.leapyear_range(1903, 1905),[1904])
        self.assertEqual(leapyear.leapyear_range(1903, 1910),[1904, 1908])
        self.assertEqual(leapyear.leapyear_range(1905, 1903),[1904])
        self.assertEqual(leapyear.leapyear_range(1910, 1903),[1904, 1908])
        self.assertEqual(leapyear.leapyear_range(1910, 1910),[])
        
        # Return is a list
        self.assertIsInstance(leapyear.leapyear_range(1903,1905), list)
        
   
if __name__ == "__main__":
    unittest.main()

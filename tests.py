# Let's import everything from conversion
from conversions import *
from conversions_refactored import convert

import unittest


class ConversionTest(unittest.TestCase):

    def test_convertCelsiusToKelvin(self):
        celsius = 0
        result = convertCelsiusToKelvin(0)
        expected = 273.15
        self.assertEqual(result, expected)

        result = convertCelsiusToKelvin(300)
        expected = 573.15
        self.assertEqual(result, expected)

    def test_convertCelsiusToFahrenheit(self):

        result = convertCelsiusToFahrenheit(0)
        expected = 32
        self.assertEqual(result, expected)

        result = convertCelsiusToFahrenheit(21)
        expected = 69.8
        self.assertEqual(result, expected)

    def test_convertFahrenheitToCelsius(self):

        result = convertFahrenheitToCelsius(32)
        expected = 0
        self.assertEqual(result, expected)

        result = convertFahrenheitToCelsius(40)
        expected = 4.444444
        self.assertAlmostEqual(result, expected, places=6)

    def test_convert(self):
        celsius = 0
        result = convert("Celsius", "Kelvin", celsius)
        expected = 273.15
        self.assertEqual(result, expected)

        celsius = 0
        result = convert("Celsius", "Fahrenheit", celsius)
        expected = 273.15
        self.assertEqual(result, expected)
        # repeat for all the rest of the temperature cases
        # do all the distance conversions


if __name__ == "__main__":
    unittest.main()

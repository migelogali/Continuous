import unittest

from task import conv_endian
from task import conv_num
from task import my_datetime


class TestCase(unittest.TestCase):
    """
    Tests for conv_endian (Function 3)
    """

    def test_conv_num1(self):
        """
        Check if string number converts to number
        """
        num_str = '1234'
        result = 1234
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num2(self):
        """
        Check if decimal string converts to decimal
        """
        num_str = '1234.5675'
        result = 1234.5675
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num3(self):
        """
        Check if negative decimal string converts to decimal
        """
        num_str = '-1234.56'
        result = -1234.56
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num4(self):
        """
        Check if negative decimal string converts to decimal
        """
        num_str = '-.45'
        result = -0.45
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num5(self):
        """
        Check if decimal trailing string converts to decimal
        """
        num_str = '123.'
        result = 123.0
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num6(self):
        """
        Check if valid hexadecimal converts (uppercase) to base 10 number
        """
        num_str = '0xAD4'
        result = 2772
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num7(self):
        """
        Check if valid hexadecimal converts (lowercase) to base 10 number
        """
        num_str = '0xad4'
        result = 2772
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num8(self):
        """
        Check if valid negative hexa converts (mixcase) to base 10 number
        """
        num_str = '-0xAd4'
        result = -2772
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num9(self):
        """
        Check if invalid hexa returns none
        """
        num_str = '-0xZd4'
        result = None
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num10(self):
        """
        Check if invalid hexa with decimal returns none
        """
        num_str = '-0xAd4.4'
        result = None
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num11(self):
        """
        Check if invalid string 2 decimals
        """
        num_str = '123.43.2'
        result = None
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num12(self):
        """
        Check if invalid string numbers and characters
        """
        num_str = '12233od'
        result = None
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num13(self):
        """
        Check if empty string returns none
        """
        num_str = ''
        result = None
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num14(self):
        """
        Check if input integer returns none
        """
        num_str = 1235
        result = None
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num15(self):
        """
        Check if hexadecimal without Ox returns None
        """
        num_str = 'AD4'
        result = None
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num16(self):
        """
        Check if hexadecimal without OX returns None
        """
        num_str = '0XAD4'
        result = 2772
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num17(self):
        """
        Check if hexadecimal without OX returns None
        """
        num_str = '-0X0'
        result = 0
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num18(self):
        """
        Check if hexadecimal without OX123 returns 291
        """
        num_str = '0X123'
        result = 291
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num19(self):
        """
        Check if hexadecimal without 0X123D4 returns 74708
        """
        num_str = '0X123D4'
        result = 74708
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num20(self):
        """
        Check if hexadecimal without 0x0000000000000F returns 15
        """
        num_str = '0x0000000000000F'
        result = 15
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num21(self):
        """
        Check if hexadecimal without 0.0 returns 0
        """
        num_str = '0.0'
        result = 0
        self.assertEqual(conv_num(num_str), result)

    def test_conv_num22(self):
        """
        Check if hexadecimal without 000.45 returns 0.45
        """
        num_str = '000.45'
        result = 0.45
        self.assertEqual(conv_num(num_str), result)

    """tests cases for function2"""

    def test_of_0(self):
        """Checks if an input of 0 seconds returns a date of 01-01-1970"""
        num_sec = 0
        result = "01-01-1970"
        self.assertEqual(my_datetime(num_sec), result)

    def test_of_123456789(self):
        """Checks if an input of 123456789 seconds returns a date of
        11-29-1973"""
        num_sec = 123456789
        result = "11-29-1973"
        self.assertEqual(my_datetime(num_sec), result)

    def test_of_9876543210(self):
        """Checks if an input of 9876543210 seconds returns a date of
        12-22-2282"""
        num_sec = 9876543210
        result = "12-22-2282"
        self.assertEqual(my_datetime(num_sec), result)

    def test_of_201653971200(self):
        """Checks if an input of 201653971200 seconds returns a date of
        02-29-8360"""
        num_sec = 201653971200
        result = "02-29-8360"
        self.assertEqual(my_datetime(num_sec), result)

    """
    Tests for conv_endian (Function 3)
    """

    def test_conv_endian1(self):
        """
        Check if endian type other than 'big' or 'little' returns None
        """
        num = 99
        endian = 'something not big or little'
        result = None
        self.assertEqual(conv_endian(num, endian), result)

    def test_conv_endian2(self):
        """
        Check if positive numbers are handled correctly in big endian
        """
        num = 954786
        endian = 'big'
        result = '0E 91 A2'
        self.assertEqual(conv_endian(num, endian), result)

    def test_conv_endian3(self):
        """
        Check if negative numbers are handled correctly in big endian
        """
        num = -954786
        endian = 'big'
        result = '-0E 91 A2'
        self.assertEqual(conv_endian(num, endian), result)

    def test_conv_endian4(self):
        """
        Check if endian type defaults to 'big' whenever endian is not specified
        """
        num = 954786
        result = '0E 91 A2'
        self.assertEqual(conv_endian(num), result)

    def test_conv_endian5(self):
        """
        Check if positive numbers are handled correctly in little endian
        """
        num = 954786
        endian = 'little'
        result = 'A2 91 0E'
        self.assertEqual(conv_endian(num, endian), result)

    def test_conv_endian6(self):
        """
        Check if negative numbers are handled correctly in little endian
        """
        num = -954786
        endian = 'little'
        result = '-A2 91 0E'
        self.assertEqual(conv_endian(num, endian), result)

    def test_conv_endian7(self):
        """
        Check if number with leading zeroes in binary is padded correctly
        """
        num = 64
        endian = 'big'
        result = '40'
        self.assertEqual(conv_endian(num, endian), result)


if __name__ == '__main__':
    unittest.main()
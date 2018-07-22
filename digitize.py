"""
https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python

Convert number to reversed array of digits
Given a random number:

C#: long;
C++: unsigned long;
You have to return the digits of this number within an array in reverse order.

Example:
348597 => [7,9,5,8,4,3]
"""

import unittest


def digitize(n):
    return list(map(int, "".join(reversed(str(n)))))


def digitize1(n):
    return map(int, str(n)[::-1])


def digitize2(n):
    return [int(x) for x in str(n)[::-1]]


class TestDigitize(unittest.TestCase):
    def test_digitize1(self):
        self.assertEqual(digitize2(35231), [1, 3, 2, 5, 3])
        pass


if __name__ == "__main__":
    print(digitize(123450))
    print(digitize1(123450))
    print(digitize2(123450))
    unittest.main()


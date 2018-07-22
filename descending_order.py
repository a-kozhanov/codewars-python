"""
https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

Descending Order
Your task is to make a function that can take any non-negative integer as a argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 21445 Output: 54421

Input: 145263 Output: 654321

Input: 1254859723 Output: 9875543221
"""
import unittest


def Descending_Order(num):
    list_numbers = [int(x) for x in str(num)[::-1]]
    list_numbers.sort(reverse=True)
    n = ""
    for x in list_numbers:
        n += str(x)
    #return "".join(map(str, list_numbers))
    return int(n)


def Descending_Order1(num):
    return int("".join(sorted(str(num), reverse=True)))


def Descending_Order2(num):
    return int(''.join(sorted(list(str(num)), reverse=True)))


def Descending_Order3(num):
    return int(''.join(sorted(str(num))[::-1]))


def Descending_Order4(num):
    strnum = ''.join(sorted(str(num), reverse = True))
    return int(strnum)


if __name__ == "__main__":
    print(Descending_Order(81529367))
    print(Descending_Order(0))
    print(Descending_Order(15))
    print(Descending_Order(123456789))
    unittest.main()


class TestDescendingOrder(unittest.TestCase):
    def test_Descending_Order(self):
        self.assertEqual(Descending_Order(0), 0)
        self.assertEqual(Descending_Order(15), 51)
        self.assertEqual(Descending_Order(123456789), 987654321)


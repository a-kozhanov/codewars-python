#!/usr/bin/python3
"""
https://www.codewars.com/kata/convert-boolean-values-to-strings-yes-or-no/train/python

Convert boolean values to strings 'Yes' or 'No'.

Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""
import unittest


def bool_to_word(boolean):
    if boolean:
        return "Yes"
    else:
        return "No"


def bool_to_word1(bool):
    return "Yes" if bool else "No"


def bool_to_word2(bool):
    if bool:
        return "Yes"
    return "No"


def bool_to_word3(bool):
    return ['No', 'Yes'][bool]


def bool_to_word4(value):
    return 'Yes' if value else 'No'


if __name__ == "__main__":
    print(bool_to_word(True), 'Yes')
    print(bool_to_word(False), 'No')




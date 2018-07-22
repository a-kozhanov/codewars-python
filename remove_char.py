"""
https://www.codewars.com/kata/remove-first-and-last-character/train/python

Remove First and Last Character

It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string.
You're given one parameter, the original string. You don't have to worry with strings with less than two characters.
"""


def remove_char(s):
    return s[1:len(s) - 1]


def remove_char1(s):
    return s[1:-1]


def remove_char2(s):
    return '' if len(s) <= 2 else s[1:-1]


if __name__ == "__main__":
    print(remove_char('eloquent'), 'loquen')
    print(remove_char('country'), 'ountr')
    print(remove_char('person'), 'erso')
    print(remove_char('place'), 'lac')
    print(remove_char('ok'), '')


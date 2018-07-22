"""
https://www.codewars.com/kata/friend-or-foe/train/python

Friend or Foe?

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

Note: keep the original order of the names in the output.
"""


def friend(x):
    result = []
    for s in x:
        if len(s) == 4:
            result.append(s)
    return result


def friend1(x):
    return [f for f in x if len(f) == 4]


def friend2(x):
    return filter(lambda name: len(name) == 4, x)


def friend3(x):
    return [y for y in x if len(y)==4]


def friend4(x):
    return list(filter(lambda s : len(s)==4 ,x))


if __name__ == "__main__":
    pass
    print(friend(["Ryan", "Kieran", "Mark"]))






from random import getrandbits


def getrandomints():
    return getrandbits(8)


def checkdelta(x, y, a):
    return 4 * pow(x, 3) + 27 * pow(y, 2) % a == 0

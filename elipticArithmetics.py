import math


def esum(a, b, p):
    return (a + b) % p


def esub(a, b, p):
    return (a - b) % p


def emul(a, b, p):
    return (a * b) % p


def efraction(a, p):
    return int(pow(a, p - 2) % p)


def epow(a, b, p):
    return pow(a, b) % p


def isrootable(a, p):
    return pow(a, p - 2) % p == 1


def esqrt(a, p):
    assert isrootable(a, p), "Non rootable value provided"
    return int(math.sqrt(a))

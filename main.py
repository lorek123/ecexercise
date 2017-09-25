from elipticArithmetics import *
from point import *
from helpers import *


def basic__operations():
    a = getrandomints()
    b = getrandomints()
    p = gen_prime(a+5, a**5)

    print("a= {} b= {} p= {}".format(str(a), str(b), str(p)))

    print("a+b= {}".format(str(esum(a, b, p))))
    print("a-b= {}".format(str(esub(a, b, p))))
    print("a*b= {}".format(str(emul(a, b, p))))
    print("a^-1= {}".format(str(efraction(a, p))))
    print("a^b= {}".format(str(epow(a, b, p))))


def points_operations():
    a = getrandomints()
    b = getrandomints()
    p1x = getrandomints()
    p1y = getrandomints()
    p2x = getrandomints()
    p2y = getrandomints()
    C = EllipticCurve(a=a, b=b)
    P = Point(C, p1x, p1y)
    Q = Point(C, p2x, p2y)
    print("P + Q = " + (P + Q))
    print("Q + P = " + (P + Q))
    print("P + Q = " + (4 * P))
    print(Q - 2 * P)


def main():
    print("Zaliczenie ćw z Przedmiotu Wykorzystanie krzywych eliptycznych w kryptografii")
    print("Artur Lorenz")

    basic__operations()
    while True:
        try:
            points_operations()
        except Exception:
            pass
        else:
            break
        finally:
            pass


if __name__ == '__main__':
    main()

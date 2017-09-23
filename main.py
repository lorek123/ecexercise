from elipticArithmetics import *
from point import *
from helpers import *


def main():
    print("Zaliczenie ćw z Przedmiotu Wykorzystanie krzywych eliptycznych w kryptografii")
    print("Artur Lorenz")

    a = getrandomints()
    b = getrandomints()
    p = getrandomints()

    print("a= {} b= {} p= {}".format(str(a), str(b), str(p)))

    print("a+b= {}".format(str(esum(a, b, p))))
    print("a-b= {}".format(str(esub(a, b, p))))
    print("a*b= {}".format(str(emul(a, b, p))))
    print("a^-1= {}".format(str(efraction(a, p))))
    print("a^b= {}".format(str(epow(a, b, p))))

    print("Point generation")
    p1 = Point()
    p1 = p1.randompoints()
    p2 = Point()
    p2 = p2.randompoints()
    print("p1: ", p1.x, p1.y)
    print("p2: ", p2.x, p2.y)
    print("p1 + p2 = ", p1 + p2)
    x = getrandomints()
    print("p1 * {} = {}".format(x, p1 * x))


if __name__ == '__main__':
    main()

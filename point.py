from helpers import *
class Point:
    def __init__(self, x=0, y=0, p=5):
        self.x = x
        self.y = y
        self.p = p

    def __repr__(self):
        return str((self.x, self.y))

    def randompoints(self):
        self.x = getrandomints()
        self.y = getrandomints()
        a = getrandomints() + 1
        p = getrandomints()
        while(not checkdelta(self.x, self.y, a)):
            self.x = getrandomints()
            self.y = getrandomints()
            a = getrandomints() + 1
        return Point(self.x, self.y)

    def __add__(self, p):
        if self.x == 0 and self.y == 0:
            return p
        if p.x == 0 and p.y == 0:
            return self
        if self.x == p.x and (self.y != p.y or self.y == 0):
            return (0, 0)
        if self.x == p.x:
            l = (3 * self.x * self.x + self.a) * inv(2 * self.y, self.q) % self.q
            pass
        else:
            l = (p.y - self.y) * inv(p.x - self.x, self.q) % self.q
            pass
        x = (l * l - self.x - p.x) % self.q
        y = (l * (self.x - x) - self.y) % self.q
        return (x, y)

    def __mul__(self, p):
        r = Point(0, 0)
        m2 = p
        n = p
        # O(log2(n)) add
        while 0 < n:
            if n & 1 == 1:
                r = r + m2
                pass
            n, m2 = n >> 1, m2 + m2
            pass
        return r

    def valid(self):
        if self == O:
            return True
        else:
            return (
                (self.y ** 2 - (self.x ** 3 + a * self.x + b)) % p == 0 and
                0 <= self.x < p and 0 <= self.y < p)

    def ec_inv(self):
        if self.x == O and self.y == 0:
            return self
        return Point(self.x, (-self.y) % self.p)

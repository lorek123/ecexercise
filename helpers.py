from secrets import randbits


def getrandomints():
    return randbits(20)


def primes_wilson(start, stop):
    """Generate the primes less than ``n`` using Wilson's theorem."""
    fac = 1
    for i in range(start, stop):
        fac *= i - 1
        if (fac + 1) % i == 0:
            return i


def gen_prime(start, stop):
    return primes_wilson(start, stop)

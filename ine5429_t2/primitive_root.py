from random import randrange


def gcd(a, b):
    if b:
        return gcd(b, a % b)
    return a


def euler_phi(n):
    return sum(gcd(i, n) == 1 for i in range(n))


def prime_factors(n):
    factors = set()
    i = 2
    while i**2 <= n:
        if n % i == 0:
            n = n//i
            factors.add(i)
        else:
            i += 1
    factors.add(n)
    return sorted(factors)


def prim_roots(n, singular=True):
    p = euler_phi(n)
    factors = prime_factors(p)
    (limit, p_roots) = (1 if singular else euler_phi(p), set())
    while len(p_roots) != limit:
        a = randrange(1, n)
        while all(pow(a, p//f, n) != 1 for f in factors):
            p_roots.add(a)
    return sorted(p_roots)

"""
Project Euler Problem 9
=======================

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


def euclid_formula(n, m):
    a = (m * m) - (n * n)
    b = 2 * (m * n)
    c = (m * m) + (n * n)

    triplet = [a, b, c]
    return triplet


def solve():
    triplets = []
    for n in range(501):
        for m in range(501):
            if m > n > 0:
                triplets.append(euclid_formula(n, m))

    return triplets[0:10]


if __name__ == "__main__":
    print(solve())

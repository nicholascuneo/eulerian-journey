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

import numpy as np


def generate_triplet(n, m):
    """
    Generates a Pythagorean triplet [a, b, c] using Euclid's Formula.

    Parameters:
    n (int): Smaller number for formula
    m (int): Larger number for formula (m > n > 0)

    Return:
    A list containing the triplet [a, b, c]

    """
    side_a = (m * m) - (n * n)  # Calculate first side of triplet
    side_b = 2 * (m * n)  # Calculate second side of triplet
    side_c = (m * m) + (n * n)  # Calculate hypotenuse side of triplet

    triplet = [side_a, side_b, side_c]
    return triplet


def find_triplet_product():
    """
    Finds product of the Pythagorean triplet [a, b, c] such that a + b + c = 1000.

    Uses Euclid's formula to generate triplets and iterates over possible values of
    n and m (ensuring m > n > 0). If a triplet with a sum of 1000 is found, the product
    of the triplet is calculated and returned.

    Return:
    The product of the triplet [a, b, c] as an integer if its sum equals 1000.
    """
    for smaller_value in range(501):  # Loop over n from 0 to 500
        for larger_value in range(501):  # Loop over m from 0 to 500
            if (
                larger_value > smaller_value > 0
            ):  # Ensure valid input for Euclid's formula
                triplet = generate_triplet(
                    smaller_value, larger_value
                )  # Generate triplet
                if sum(triplet) == 1000:  # Check if sum of triplet = 1000
                    return np.prod(triplet)  # Calculate and return product of triplet


if __name__ == "__main__":
    print(find_triplet_product())

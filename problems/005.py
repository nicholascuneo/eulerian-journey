"""
Project Euler Problem 5
=======================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""


def is_divisible_by_all(number, divisors):
    """
    Checking if a given number is evenly divisible by all divisors in a
    givenlist without any remainder.

    args: Given number, list of divisors

    Return False if number is not divisible by a divisor
    Return True if a number is divisible by all divisors
    """

    for divisor in divisors:
        if number % divisor != 0:
            return False
    return True


def solve():
    """
    Find the smallest number divisible by all numbers from 1 to 20.

    Starts from 20 and checks each number until one is found that all divisors
    can divide evenly.

    Return smallest number that meets the condition.
    """
    start = 20  # Begin at largest divisor for efficiency
    divisors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    while True:
        # Check if current number is divisible by all divisors
        if is_divisible_by_all(start, divisors):
            return start  # Return number once found
        start += 1  # Increment to check next number


if __name__ == "__main__":
    print(solve())

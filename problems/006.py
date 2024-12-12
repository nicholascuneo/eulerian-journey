"""
Project Euler Problem 6
=======================

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""

def calculate_difference():
    """
    Function to return the difference of the sum of squares of the first
    100 natural numbers and the square of the sum of the first 100 natural
    numbers.
    """

    # Calculate sum of square of the first 100 natural numbers
    sum_of_squares = sum(number ** 2 for number in range(101)) # Use list comprehension
    
    # Calculate sum and square of the sum of the first 100 natural numbers
    total_sum = sum(range(101))
    square_of_sum = total_sum ** 2

    # Calculate difference between square of sum and sum of squares
    difference = square_of_sum - sum_of_squares

    return difference

if __name__ == "__main__":
    print(calculate_difference())
"""
Project Euler Problem 1
=======================

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def solve(number):
    # Initialize sum variable
    sum = 0
    
    # Loop through starting from 0 up until, but not including input number
    for i in range(number):
        # Check if i is divisible by 3 or 5 with no remainder
        if i % 3 == 0 or i % 5 == 0:
            # If no remainder, add to sum
            sum += i
    
    return sum

if __name__ == "__main__":
    print(solve(1000))
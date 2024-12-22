"""
Project Euler Problem 10
========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def sum_of_primes(limit):
    """
    Calculate the sum of all prime numbers below a given limit.

    Parameters:
    limit (int): The upper limit (exclusive) for calculating primes.

    """

    primes = [2]  # Initialize list of primes with the first prime number, 2
    start = 3  # Check prime candidates starting from next integer

    # Iterate over candidate numbers up to sepcified limit
    for _ in range(2, limit):
        is_prime = True
        # Check divisibility up to the square root of current number
        for divisor in range(2, int(start**0.5) + 1):
            if start % divisor == 0:  # Not prime if divisible
                is_prime = False
                break  # Exit loop early since start is not prime
        if is_prime:
            primes.append(start)  # Add prime to list

        start += 1  # Increment to next candidate number

    return sum(primes)  # Return sum of all identified primes


if __name__ == "__main__":
    print(sum_of_primes(2000000))

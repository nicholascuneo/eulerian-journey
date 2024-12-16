"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""


def find_prime_number():
    """
    Finds the 10,001st prime number using a while loop to generate prime numbers, and
    stops once the 10,001st prime is found.
    """
    primes = [2]  # List to store prime numbers, starting with first prime
    start = 3  # Begin checking candidates from next integer

    while len(primes) < 10001:
        is_prime = True
        # Check divisibility of start by all numbers up to its square root
        for divisor in range(2, int(start**0.5) + 1):
            if start % divisor == 0:  # Not prime if divisible
                is_prime = False
                break  # Exit loop since start is not prime
        if is_prime:
            primes.append(start)  # Add prime to list

        start += 1  # Increment to next candidate number

    return primes[-1]  # Return last prime in list


if __name__ == "__main__":
    print(find_prime_number())

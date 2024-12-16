"""
Project Euler Problem 7
=======================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10001st prime number?
"""


def find_prime_number(number):
    """
    Finds the Nth prime number using a while loop to generate list of prime numbers,
    stopping once the Nth prime is found.
    """

    primes = [2]  # List to store prime numbers, starting with first prime
    start = 3  # Begin checking candidates from next integer

    while len(primes) < number:  # Generate primes until required count is reached
        is_prime = True
        # Check divisibility of start by all numbers up to its square root
        for divisor in range(2, int(start**0.5) + 1):
            if start % divisor == 0:  # Not prime if divisible
                is_prime = False
                break  # Exit loop since start is not prime
        if is_prime:
            primes.append(start)  # Add prime to list

        start += 1  # Increment to next candidate number

    return primes[-1]  # Return the Nth prime number


if __name__ == "__main__":
    # Get user input for which prime number to find
    user_number = int(input("Enter the prime number would you like to find: "))
    print(find_prime_number(user_number))

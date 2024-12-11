"""
Project Euler Problem 3
=======================

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def max_prime_factor(number):
    """
    Finds the largest prime factor of a given number.
    """
    
    prime_candidates = [] 
    max_limit = int(number ** 0.5) # No need to check factors beyond sqrt of number

    # Generate list of prime candidates up to sqrt of number
    for candidate in range(2, max_limit + 1): # Check integers from 2 up to sqrt of number
        is_prime = True
        for divisor in range(2, int(candidate ** 0.5) + 1): # Test divisors up to sqrt of candidate
            if candidate % divisor == 0: # Candidate not prime if divisible
                is_prime = False
                break # Exit since candidate is not prime
        if is_prime:
                prime_candidates.append(candidate) # Add prime to list

    prime_factors = []

    # Check which primes are factors of given number
    for prime in prime_candidates:
        if number % prime == 0: # If divsible, is a prime factor of given number
             prime_factors.append(prime)

    # Find and return largest prime factor of given number
    largest_prime_factor = max(prime_factors)
    return largest_prime_factor
     
if __name__ == "__main__":
    print(max_prime_factor(600851475143))
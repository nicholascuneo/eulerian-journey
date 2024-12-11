"""
Project Euler Problem 4
=======================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def max_palindrome():
    """
    Finds largest palindrome that is made from the product of two
    3-digit numbers.
    """

    three_digit_nums = []
    # Generate list of 3-digit numbers
    for number in range(100, 1000):
        three_digit_nums.append(number)

    palindromes = []
    
    # Generate list of palindromic number made from product of 3 digit numbers
    for num in three_digit_nums:
        multiplier = 100 # Reset multiplier for each number
        while multiplier < 1000: # Can only multiply by 3-digit numbers
            candidate = (num * multiplier)

            # If result is palindromic, add to list
            if len(str(candidate)) == 5: # 5 digit results
                if (str(candidate)[0] == str(candidate)[4]) and (str(candidate)[1] == str(candidate)[3]):
                    palindromes.append(candidate)
            if len(str(candidate)) == 6: # 6 digit results
                if (str(candidate)[0] == str(candidate)[5]) and (str(candidate)[1] == str(candidate)[4]) and (str(candidate)[2] == str(candidate)[3]):
                    palindromes.append(candidate)
            
            multiplier += 1 # Increment multiplier by 1 while looping on num
    
    # Find and return largest palindrome that is a product of two 3-digit numbers
    largest_palindrome = max(palindromes)
    return largest_palindrome

if __name__ == "__main__":
    print(max_palindrome())
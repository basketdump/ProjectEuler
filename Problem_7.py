'''
Problem 7 of Project Euler
--------------------------
By listing the first six prime numbers: 
2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10,001st prime number?
'''

# What we know:
#   1. A prime number is only divisible by 1 and itself.

# Functions we'll need
#   1. is_prime(number) which will determine if number is prime or not.
#   We know we can skip by 2 starting at 3 (3, 5, 7, etc...)

#TODO: See if there is a formula for calculating nth prime.


def is_prime(number):
    '''returns True if number is prime otherwise returns False'''
    if number % 2 == 0 or number < 2:
        return False
    for i in range(3, number, 2):
        if number % i == 0:
            return False
    return True


def main():
    '''main is our initial function to be ran.
    it will have a loop construct that will be
    ran until our list of primes has a length
    of n_prime'''
    n_prime = 10001
    primes = [2, 3]
    current_number = 5
    while len(primes) < n_prime:
        while not is_prime(current_number):
            current_number += 1
        primes.append(current_number)
        current_number += 1
    print(primes)
    print(primes[len(primes) - 1])
    print(len(primes))

main()

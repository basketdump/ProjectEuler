'''
Problem 3 of Project Euler
--------------------------
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''

def is_prime(number):
    '''this function determines if number is a prime number by bruteforce'''
    if number < 2:
        return False
    elif number == 2 or number == 3:
        return True

    if number % 2 == 0:
        return False

    for i in range(3, number, 2):
        if number % i == 0:
            return False

    return True


def prime_factor(number):
    '''returns the lowest prime factor of a number and the other factor as a list'''
    for i in range(number):
        if is_prime(i) and number % i == 0:
            return [i, number // i]



def main():
    '''cycles through prime factors and appends them to primes_found until
    both factors are found to be prime (no more factorization)'''
    number = int(1234567891231212)
    primes_found = []
    while not is_prime(number):
        factors = prime_factor(number)
        primes_found.append(factors[0])
        number = factors[1]
    primes_found.append(number)
    print(max(primes_found))

main()

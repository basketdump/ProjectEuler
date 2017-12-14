'''
Problem 5 of Project Euler
--------------------------
2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''

# what we know:
#   we can step by highest number (20)
#   we don't have to check by factors of 20
#       1, 2, 4, 5, 10, 20


def check_remainders(number, divisors):
    '''returns True if number is evenly dividable by each
    divisor in the divisors list'''
    for divisor in divisors:
        if number % divisor != 0:
            return False
    return True


def generate_divisors(number):
    '''generates a list of numbers (1-number) that do not divide evenly
    into number'''
    divisors = []
    for i in range(1, number + 1):
        if number % i != 0:
            divisors.append(i)
    return divisors


def main():
    '''main function to step (max_divisor) through numbers looking for answer'''
    max_divisor = 30
    divisors = generate_divisors(max_divisor)
    print(divisors)
    answer = max_divisor
    while not check_remainders(answer, divisors):
        answer = answer + max_divisor
    print(answer)


main()

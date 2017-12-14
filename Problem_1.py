'''
Problem 1 of Project Euler
--------------------------
If we list all the natural numbers
below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''

def get_multiples_below(factors, max_value):
    '''returns a list of numbers that are
    below max_value and multiples of factor(s)'''
    multiples = []
    for i in range(1, max_value):
        for factor in factors:
            if i % factor == 0:
                multiples.append(i)
                break
    return multiples


def main():
    '''defines max_value, factors as a list of factors we will accept for
    finding multiples, and multiples is our list of mulitples that are
    integers that are multiples of at least one of the factors and
    below max_value. answer is the sum of all multiples '''
    max_value = 1000
    factors = [3, 5]
    multiples = get_multiples_below(factors, max_value)
    answer = sum(multiples)
    print(answer)


main()

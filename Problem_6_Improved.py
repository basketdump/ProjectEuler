'''
Problem 6 of Project Euler
--------------------------
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of
the first ten natural numbers and the square of the sum
is 3025 − 385 = 2640.

Find the difference between the sum of the squares of
the first one hundred natural numbers and the square
of the sum.
'''

# answer: (1 + ... + n)^2 - (1^2 + ... + n^2)
# we need to do three things
    # 1. Square (built-in)
    # 2. Sum (built-in)
    # 3. Define square_of_sums and sum_of_squares


def sum_of_squares(number):
    '''this function calculates the sum of squares
    for numbers 1 through number'''
    if number > 1:
        return number ** 2 + sum_of_squares(number - 1)
    else:
        return 1


def square_of_sums(number):
    '''this function calculates and returns the
    square of the sum for numbers 1 through number'''
    return sum(list(range(1, number+1))) ** 2


def main():
    '''our main function that finds the answer which is
    the difference between the square of sums and
    sum of squares for 1-number where number is 100'''
    number = 100
    answer = square_of_sums(number) - sum_of_squares(number)
    print(answer)


main()

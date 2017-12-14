'''
Problem 4 of Project Euler
--------------------------
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def reverse_list(target_list):
    '''returns a list with the reversed ordering of target_list'''
    target_list_reversed = []
    for i in range(len(target_list) - 1, -1, -1):
        target_list_reversed.append(target_list[i])
    return target_list_reversed


def is_palindrome(target_list):
    '''this function returns True if target_list(list) is a
    palindrome or False if target_list is not a palindrome'''
    target_list_reversed = reverse_list(target_list)
    return target_list == target_list_reversed


def int_to_list(number):
    '''returns an integer in the form of a list i.e. (101 = [1, 0, 1])'''
    number_list = []
    while number > 0:
        number_list.append(number % 10)
        number = number // 10
    return number_list


def main():
    '''cycles through every possibility of 3 digit factors for num1 and num2'''
    starting_number = 999999
    lowest_multiple = 1
    while starting_number / lowest_multiple > 10:
        lowest_multiple *= 10
    print(lowest_multiple)
    num1 = starting_number
    num2 = starting_number
    highest = 0

    # while loop to cycle through each num1 and num2 possiblity
    while num1 > lowest_multiple:
        while num2 > lowest_multiple:
            product = num1 * num2
            # if product is less than our highest, we can break the num2 while loop
            # because every other product in this current loop will be less than our highest so
            # it does not matter if it's palindromic at this point.
            if product > highest:
                if is_palindrome(int_to_list(product)):
                    highest = product
            else:
                break
            num2 = num2 - 1
        num2 = starting_number
        num1 = num1 - 1

    print(highest)


main()

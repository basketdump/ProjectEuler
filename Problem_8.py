# -*- coding: utf-8 -*-
"""
Project Euler

Problem 8
---------------

The four adjacent digits in the 1000-digit number that have the
greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?
"""

# What we know
#   1. We will need to do groupings of 13.
#   2. We can only move over one digit at a time.
#   3. We will need something to track the highest product (thus far).
#   4. We can skip a grouping if it contains a 0. (found this out midway)

# We need:
#   1. A function to find the product of each digit in a string of numbers.
#   2. A loop to cyle through the length of the given input
#   3. A single line of input
#   4. An if statement to skip grouping if zero exists.

# Speed:
#   a. n*group_size iterations - or 13,000 iterations worst case. (no zeros)


def calculate_product(number):
    '''this function will take a number as a string and find the product
    of all digits within that number (e.g. 123 = 1 * 2 * 3)'''
    product = 1
    for n in number:
        product *= int(n)
    return product


def main():
    '''our main function for this problem. it will format the input, cycle
    through each grouping of 13 number in the input, and print the highest
    returned value of calculate_product(number).'''
    
    group_size = 13 # size of grouping (e.g. 3 for 12345 will be 123, 234, etc)
    highest_product = 0 # records highest returned value of calculate_product
    
    number = """73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450"""
                
    number = number.replace('\n', '') # formats string to single line
    
    # loop through each grouping with len(number) - group_size being the last
    # digit that can begin a grouping of group_size
    for i in range(0, len(number) - group_size, 1):
        sub_number = number[i:i+group_size] # our current group
        
        # the code below checks to see if 0 exists within the current group
        # if it does, then skip to the 0 and let the for loop start at the
        # index promptly after. 0 * anything is ZERO
        zero_exists = sub_number.find('0')
        if zero_exists != -1:
            i += zero_exists
            zero_exists = -1
        else: # if no zero's exist in current group, check product
            product = calculate_product(sub_number)
            if product > highest_product:
                highest_product = product
    
    print(highest_product)


main()
    

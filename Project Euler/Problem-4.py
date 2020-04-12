#!/usr/bin/env python3
# coding=UTF-8

"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""


def max_palindrome(n):
    palindromes = set()
    for x in range(n + 1):
        for y in range(n + 1):
            if str(x * y) == str(x * y)[::-1] and len(str(x * y)) > 1:
                palindromes.add(x * y)
    return max(palindromes)


print(max_palindrome(999))

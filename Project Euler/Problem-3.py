#!/usr/bin/env python3
# coding=UTF-8

"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""


def is_prime(n):
    if n % 2 == 0:
        return False
    for i in range(3, int(n * 0.5) + 1, 2):
        print(i)
        if n % i == 0:
            return False
    return True


def primes(n):
    factors = list()
    for i in range(3, int(n / 2) + 1, 2):
        print(i)
        if n % i == 0 and is_prime(i):
            factors.append(i)
        print(factors)
    return factors


print(max(primes(600851475143)))

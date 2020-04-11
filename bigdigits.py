#!/usr/bin/env python3
# coding=UTF-8

import sys

zero = ["    **    ",
        "  *    *  ",
        " *      * ",
        " *      * ",
        "  *    *  ",
        "    **    "]

Digits = [zero]

try:
    digits = sys.argv[1]
    row = 0
    while row < len(Digits[0]):
        line = ""
        column = 0
        while column < len(digits):
            number = int(digits[column])
            digit = Digits[number]
            line += digit[row] + " "
            column += 1
        print(line)
        row += 1
except IndexError:
    print("Index error")
except ValueError:
    print("Value error")

#!/usr/bin/python3

import sys


def is_palindrome(word):
    return word == word[::-1]

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        word = word.lower()
        if is_palindrome(word):
            print(f"{word}\tTrue")
        else:
            print(f"{word}\tFalse")

#!/usr/bin/python3

import sys

current_word = None
current_count = 0
current_value = None

for line in sys.stdin:
    line = line.strip()
    word, value = line.split("\t", 1)
    if current_word != word:
        if current_word:
            print(f"{current_word} {current_value} {current_count}")
        current_word = word
        current_count = 1
        current_value = value
    else:
        current_count += 1

if current_word:
    print(f"{current_word} {current_value} {current_count}")

#!/usr/bin/python3

import sys

def mapper():
    for line in sys.stdin:
        values = line.strip().split()
        for value in values:
            
            # Keluarkan pasangan key-value (key: 'value', nilai: 90)
            print('nilai', value)


mapper()

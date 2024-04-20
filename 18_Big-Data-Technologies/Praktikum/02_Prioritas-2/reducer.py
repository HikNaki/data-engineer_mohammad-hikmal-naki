#!/usr/bin/python3

import sys

def reducer():
    total = 0
    count = 0
    current_key = None

    for line in sys.stdin:
        key, value = line.strip().split()
        
        # Mengecek apakah key telah berubah
        if key != current_key:
            if current_key:
                print(current_key, total / count)
            current_key = key
            total = 0
            count = 0

        # menambahkan nilai ke total dan increment count
        total += float(value)
        count += 1

    # menghitung rata-rata untuk key terakhir
    if current_key:
        print(current_key, total / count)

reducer()

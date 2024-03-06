
#NO 2 Soal Prioritas 2

def prime_rectangle(height, width, start):
    def is_prime (x):
        if x < 2:
            return False
        
        for i in range(2, x):
            if x % i == 0:
                return False

        return True
    
    
    current_number = start + 1
    total_sum = 0
    for i in range(width):
        row = []
        for j in range(height):
            while not is_prime(current_number):
                current_number += 1
            row.append(current_number)
            total_sum += current_number
            current_number += 1
        print(*row)
    return total_sum


print(prime_rectangle(2, 3, 13))
print("")
print(prime_rectangle(5,2,1))


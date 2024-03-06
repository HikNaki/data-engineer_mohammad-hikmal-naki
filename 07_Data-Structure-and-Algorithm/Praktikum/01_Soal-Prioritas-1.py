
#NO 1 Soal Prioritas 1

def group_numbers(numbers, target):

  groups = [[], []]
  for num in numbers:
    if num % target == 0:
      groups[0].append(num)
    else:
      groups[1].append(num)
  return groups


print(group_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
print(group_numbers([23, 15, 19, 20, 75, 30, 45], 5))

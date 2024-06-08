def min_max_numbers(sequence_list):
    sequence_str = ''.join(map(str, sequence_list))
    min_number = ''.join(sorted(sequence_str))
    max_number = ''.join(sorted(sequence_str, reverse=True))
    return min_number, max_number

sequence_one = [2, 0, 509, 23]
sequence_two = [45, 0, 14, 8, 1]

min_max_one = min_max_numbers(sequence_one)
min_max_two = min_max_numbers(sequence_two)

print(min_max_one)
print(min_max_two)

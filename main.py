print("Приступаем к выполнению")
# задача1

def combine_lists(list1, list2):
    combined_list = []
    if len(list1) != len(list2):
        raise ValueError("Длины списков должны быть одинаковыми")
    for i in range(len(list1)):
        combined_list.append(list1[i])
        combined_list.append(list2[i])
    return combined_list

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

combined = combine_lists(list1, list2)
print(combined)

# задача 2

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


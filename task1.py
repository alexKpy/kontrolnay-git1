# задача 1

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

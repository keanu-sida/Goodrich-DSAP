def reverse_list(data):
    reversed_list = []
    for i in range(len(data) - 1, -1, -1):
        reversed_list.append(data[i])
    return reversed_list

list1 = [1, 2, 3, 4, 5, 6]

print(reverse_list(list1))
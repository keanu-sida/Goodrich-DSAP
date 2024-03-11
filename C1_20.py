import random
# def my_shuffle(nums):
#     new_order = []
#     for i in range(len(nums)):
#         index = random.randint(0, len(nums) - 1)
#         if index not in new_order:
#             new_order.append(index)
#         while index in new_order:
#             index = random.randint(0, len(nums) - 1)
#             if index not in new_order:
#                 new_order.append(index)
#     shuffled_nums = nums[new_order]
#     return shuffled_nums

# list1 = [1, 2, 3, 4, 5, 6]
# print(my_shuffle(list1))

def my_shuffle(nums):
    new_nums = []
    for i in range(len(nums)):
        index = random.randint(0, len(nums) - 1)
        new_nums.append(nums[index])
        nums.remove(nums[index])
    return new_nums

list1 = [1, 2, 3, 4, 5, 6]
print(my_shuffle(list1))
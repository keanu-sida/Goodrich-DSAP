def are_distinct(nums):
    length1 = len(nums)
    if length1 == len(list(set(nums))):
        return True
    return False

testTrue1 = [1, 2, 3, 4]
testTrue2 = [1, 3, 5, 6]
testFalse1 = [1, 2, 5, 6, 7, 7]
testFalse2 = [1, 4, 5, 5, 7, 1]

print(are_distinct(testTrue1))
print(are_distinct(testTrue2))
print(are_distinct(testFalse1))
print(are_distinct(testFalse2))
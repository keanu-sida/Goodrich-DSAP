def distinct_nums(nums):
    nums = list(set(nums))
    counter = 0
    for i in range(len(nums)):
        if nums[i] % 2 == 1:
            counter += 1
            if counter == 2:
                return True
    return False

testTrue1 = [1, 2, 3, 4, 5]
testTrue2 = [1, 3, 5]
testFalse1 = [1, 2, 4, 6]
testFalse2 = [1, 1, 1]

print(distinct_nums(testTrue1))
print(distinct_nums(testTrue2))
print(distinct_nums(testFalse1))
print(distinct_nums(testFalse2))
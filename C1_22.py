## Write a short program that takes two arrrays a and b of length n storing int values and returns an array c of the dot product of a and b. (c[i] = a[i] * b[i] for 0 <= i < n)

### define function with parameters a and b
def my_dot_product(a, b):
### use list comprehension to generate new array, then return it
    c = [a[i]*b[i] for i in range(0, len(a))]
    return c

### test case
nums1 = [0, 1, 2]
nums2 = [3, 4, 5]

### call function
print(my_dot_product(nums1, nums2))

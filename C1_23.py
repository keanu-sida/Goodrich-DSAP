## Give an example of a Python code fragment that attempts to write an element to a list based on an index that may be out of bounds. If so, the program should catch the exception and print "Eoror! Out of bounds!"

# initalize an arbitrary number for length of array, then create it with values corresponding to indices
n = 10
nums = [i for i in range(n)]

### define a for loop with range that goes one iteration over the length of the array
for i in range(0, n + 1):
### use try-except to catch index error
    try:
### add 10 to each index
        nums[i] = i + 10
        print(nums[i])
### print error message once exception is met
    except IndexError:
        print("Error! Out of bounds.")


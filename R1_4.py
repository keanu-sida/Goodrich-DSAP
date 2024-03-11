# Write a fxn that takes a positive integer n and returns the sum of the squares of all positive integers smaller than n.
def squaresums(n):
    ans = 0
    for i in range(1, n + 1):
        ans += (i*i)
    return ans

print(squaresums(3))
print(squaresums(4))
print(squaresums(5))

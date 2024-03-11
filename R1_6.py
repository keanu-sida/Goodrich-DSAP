def odd_square_sum(n):
    ans = 0
    for i in range(1, n, 2):
        ans += (i*i)
    return ans
print(odd_square_sum(4))
print(odd_square_sum(5))
print(odd_square_sum(6))

odd_square_sum1 = sum(i*i for i in range(1, 4, 2))
odd_square_sum2 = sum(i*i for i in range(1, 5, 2))


n = 6
odd_square_sum = sum(i*i for i in range(1, n, 2))

expt = (i*i for i in range(1, 6, 2))
print(expt) 

print(odd_square_sum)
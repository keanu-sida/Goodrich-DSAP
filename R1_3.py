list1 = [1, 6, 10, -156, 2, -1]

def minmax(list):
    ans = [list[0], list[0]]
    for num in list:
        if num < ans[0]:
            ans[0] = num
        if num > ans[1]:
            ans[1] = num
    return tuple(ans)

print(minmax(list1))
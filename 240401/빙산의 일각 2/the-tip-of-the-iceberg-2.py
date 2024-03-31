n = int(input())
array = [int(input()) for _ in range(n)]

max_num = 0
for water in range(min(array), max(array)):
    check = False
    num = 0
    for i in range(len(array)):
        if array[i] >= water and check is False:
            check = True
            num += 1
        elif array[i] < water:
            check = False
    max_num = max(num, max_num)

print(max_num)
n, b = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(n)]


max_cnt = 0
for i in range(n):
    array[i][0] //= 2
    cnt = 0
    price = 0
    for student in sorted(array, key = lambda x : x[0] + x[1]):
        if price + student[0] + student[1] <= b:
            cnt += 1
            price += student[0] + student[1]
    max_cnt = max(max_cnt, cnt)
    array[i][0] *= 2

print(max_cnt)
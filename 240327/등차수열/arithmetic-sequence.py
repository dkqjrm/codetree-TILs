n = int(input())
array = list(map(int, input().split()))
max_cnt = 0
for k in range(min(array), max(array) + 1):
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if abs(array[i] - k) == abs(array[j] - k):
                cnt += 1

    max_cnt = max(cnt, max_cnt)

print(max_cnt)
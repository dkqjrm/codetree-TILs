n, k = map(int, input().split())
array = [int(input()) for _ in range(n)]
max_cnt = 0

for i in range(len(array)): # 인덱스 i는 최솟값
    cnt = 0
    for j in range(len(array)):
        if 0 <= array[j] - array[i] and array[j] - array[i] <= k:
            cnt += 1
    max_cnt = max(cnt, max_cnt)

print(max_cnt)
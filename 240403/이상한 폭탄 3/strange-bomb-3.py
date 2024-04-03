n, k = map(int, input().split())
array = [int(input()) for _ in range(n)]

bomb = {}

for i in range(1, max(array) + 1): # 조사할 정수
    now = -1e12
    for idx, num in enumerate(array):
        if num == i:
            distance = idx - now
            if distance <= k:
                if i not in bomb.keys():
                    bomb[i] = 1
                else:
                    bomb[i] += 1
            now = idx

print(sorted(bomb.items(), key = lambda x : -x[1])[0][1])
n, k = map(int, input().split())
array = [int(input()) for _ in range(n)]

bomb_dict = {}

for i in range(1, max(array) + 1): # 조사할 정수
    now = -1e12
    bomb = [0] * 1000
    for idx, num in enumerate(array):
        if num == i:
            distance = idx - now
            if distance <= k:
                bomb[now] = 1
                bomb[idx] = 1
            now = idx
    bomb_dict[i] = sum(bomb)
if sum(bomb_dict.values()) == 0:
    print(0)
else:
    print(sorted(bomb_dict.items(), key = lambda x : (-x[1], -x[0]))[0][0])
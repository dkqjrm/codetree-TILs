n, k = map(int, input().split())

array = [0] * (n + 5)

for idx in range(n):
    num = int(input())
    array[idx] = num

bomb_list = []
for i in range(n):
    for j in range(i + 1, n):
        if array[i] == array[j] and j - i <= k:
            bomb_list.append(array[i])

print(max(bomb_list))
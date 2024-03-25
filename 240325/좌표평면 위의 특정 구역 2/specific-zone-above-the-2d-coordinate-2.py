n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

result = 1e9
for i in range(n): # 0, 1, 2, 3
    x_list = []
    y_list = []
    for j in range(n): # 0, 1, 2, 3
        if i == j: # 1, 2, 3 // 0, 2, 3 // 0, 1, 3 // 0, 1, 4
            continue

        else:
            x_list.append(array[j][0])
            y_list.append(array[j][1])
    result = min((max(x_list) - min(x_list)) * (max(y_list) - min(y_list)), result)

print(result)
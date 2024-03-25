n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

min_length = 1e13
for i in array:
    for j in array:
        if i != j:
            min_length = min(min_length, ((i[0]-j[0]) ** 2) + ((i[1]-j[1]) ** 2))

print(min_length)
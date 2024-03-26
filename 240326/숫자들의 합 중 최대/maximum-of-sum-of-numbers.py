x, y = map(int, input().split())

max_result = 0
for i in range(x, y+1):
    strnum = str(i)
    result = 0
    for j in strnum:
        result += int(j)
    max_result = max(max_result, result)

print(max_result)
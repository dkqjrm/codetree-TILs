n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

def check(a, b, c): # x가 같은 게 2개 이상, y가 같은 게 2개 이상
    if a[0] == b[0] and b[1] == c[1]:
        return abs(b[1] - a[1]) * abs(c[0] - b[0])
    elif a[0] == b[0] and a[1] == c[1]:
        return abs(b[1] - a[1]) * abs(c[0] - a[0])
    elif a[0] == c[0] and a[1] == b[1]:
        return abs(a[1] - c[1]) * abs(b[0] - a[0])
    elif a[0] == c[0] and b[1] == c[1]:
        return abs(a[1] - c[1]) * abs(c[0] - b[0])
    elif b[0] == c[0] and a[1] == b[1]:
        return abs(b[1] - c[1]) * abs(b[0] - a[0])
    elif b[0] == c[0] and a[1] == c[1]:
        return abs(b[1] - c[1]) * abs(a[0] - c[0])
    else:
        return 0
        
result = 0

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            result = max(result, check(array[i], array[j], array[k]))
                
print(result)
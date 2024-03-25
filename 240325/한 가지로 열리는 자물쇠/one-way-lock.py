n = int(input())

a, b, c = map(int, input().split())

result = 0 
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if abs(a - i) <= 2:
                result += 1
            elif abs(b - j) <= 2:
                result += 1
            elif abs(c - k) <= 2:
                result += 1

print(result)
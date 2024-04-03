a, b = map(int, input().split())
c, d = map(int, input().split())

if b < c or d < a:
    result = b - a + d - c
elif c < b and b < d:
    result = c - a + b - c + d - b
elif a < d and d < b:
    result = a - c + d - a + b - d

elif a < c and d < b:
    result = b - a
elif c < a and b < d:
    result = d - c

print(result)
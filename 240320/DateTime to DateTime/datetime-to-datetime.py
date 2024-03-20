a, b, c = map(int, input().split())

# 11 11 - 671
# 24시간 1440

result = (a * 24 * 60 + b * 60 + c) - (11 * 24 * 60 + 11 * 60 + 11)

if result < 0:
    print(-1)
else:
    print(result)
a, b, c = map(int, input().split())

# 11 11 - 671
# 24시간 1440

if a == 11:
    print(b * 60 + c - 671)
elif a == 12:
    print(769 + b * 60 + c)
else:
    print(769 + 1440 + b * 60 + c)
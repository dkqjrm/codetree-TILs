n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

def check(i, j, k, n, num):
    if (abs(num[0] - i) <= 2) or (n - abs(num[0] - i) <= 2):
        if (abs(num[1] - j) <= 2) or (n - abs(num[1] - j) <= 2):
            if (abs(num[2] - k) <= 2) or (n - abs(num[2] - k) <= 2):
                return 1
    else:
        return 0


result = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if check(i, j, k, n, A) or check(i, j, k, n, B):
                result += 1


print(result)
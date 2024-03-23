n = int(input())
array = [int(input()) for _ in range(n)]

def solve(num1, num2, num3):
    while num1 != 0 and num2 != 0 and num3 != 0:
        if num1 % 10 + num2 % 10 + num3 % 10 > 10:
            return False
        else:
            num1 //= 10
            num2 //= 10
            num3 //= 10
    return True

result = -1
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # i, j, k는 각각 숫자임
            if solve(array[i], array[j], array[k]):
                result = max(result, array[i]+array[j]+array[k])

print(result)
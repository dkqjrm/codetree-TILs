a, b = map(int, input().split())
n = int(input())

def convert_ten(n, a):
    # a -> 10
    result = 0
    mul = 1
    while True:
        result += (n % 10) * mul
        n //= 10
        mul *= a
        if n == 0:
            break
    return result

def convert_b(n, b):
    result = []
    while True:
        if n < b:
            result.append(n)
            break
        result.append(n % b)
        n //= b

    return result[::-1]

for i in convert_b(convert_ten(n, a), b):
    print(i, end='')
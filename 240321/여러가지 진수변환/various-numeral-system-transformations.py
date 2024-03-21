n, b = map(int, input().split())

def convert(n, b):
    result = []
    while True:
        if n < b:
            result.append(n)
            break
        result.append(n % b)
        n //= b

    return result[::-1]

for i in convert(n, b):
    print(i, end='')
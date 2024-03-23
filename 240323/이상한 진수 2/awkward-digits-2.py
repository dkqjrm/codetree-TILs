a = list(input())

def convert_ten(a):
    result = 0
    for i in a:
        result *= 2
        result += int(i)
    return result

result = 0

for idx in range(len(a)):
    a[idx] = (int(a[idx]) + 1) % 2
    result = max(result, convert_ten(a))
    a[idx] = (int(a[idx]) + 1) % 2

print(result)
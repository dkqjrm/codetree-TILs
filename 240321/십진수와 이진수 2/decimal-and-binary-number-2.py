n = int(input())

def convert_ten(n):
    result = 0
    mul = 1
    while n != 0:
        result += (n % 10) * mul
        n //= 10
        mul *= 2
    return result

def convert_two(n):
    result = []
    while True:
        if n < 2:
            result.append(n)
            break
        result.append(n % 2)
        n //= 2
    return result[::-1]

inter_result = convert_ten(n) * 17

for i in convert_two(inter_result):
    print(i, end='')
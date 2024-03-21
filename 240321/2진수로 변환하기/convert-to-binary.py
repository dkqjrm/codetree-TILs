n = int(input())

def convert(n):
    digits = []
    while True:
        if n >= 2:
            digit = n % 2
            n //= 2
            digits.append(digit)

        else:
            digits.append(digit)
            break

    return (digits[::-1])

for digit in convert(n):
    print(digit, end="")
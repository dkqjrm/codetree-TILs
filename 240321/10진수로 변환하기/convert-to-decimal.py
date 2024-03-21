n = int(input())

result = 0
for i in str(n):
    result = result * 2 + int(i)

print(result)

# result = 0
# mul = 1
# while n != 0:
#     result += (n % 10) * mul
#     n //= 10
#     mul *= 2
# print(result)
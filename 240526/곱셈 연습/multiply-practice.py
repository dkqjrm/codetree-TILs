n = int(input())
m = int(input())

a = n * (m % 10)
b = n * (m // 10 % 10)
c = n * (m // 100)
d = a + b * 10 + c * 100

print(a)
print(b)
print(c)
print(d)
a, b, c = map(int, input().split())

def solution(num):
    if num % 2 == 0:
        return num // 2
    else:
        return num * 3 - 20

a = solution(a)
b = solution(b)
c = solution(c)

print(a, b, c)
n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

def check(n):
    cnt = 0
    for tmp in array:
        a, b, c = tmp[0], tmp[1], tmp[2]
        if a == n:
            n = b
        elif b == n:
            n = a
        
        if n == c:
            return cnt
        else:
            cnt += 1

    return 0

max_cnt = 0
for i in range(1, 3 + 1):
    max_cnt = max(max_cnt, check(i))

print(max_cnt)
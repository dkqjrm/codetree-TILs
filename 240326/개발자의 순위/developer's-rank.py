k, n = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(k)]

cnt = 0

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a != b:
            check = False
            for arr in array:
                if arr.index(a) > arr.index(b):
                    check = True
            if check == False:
                cnt += 1


print(cnt)
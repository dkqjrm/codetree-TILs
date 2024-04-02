n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

# 하지만 사사분면 ++ -+ -- +-

min_m = 1e12

for x in range(0, 101):
    for y in range(0, 101):
        pp = 0
        mp = 0
        mm = 0
        pm = 0
        for i in array:
            if i[0] < x and i[1] < y:
                mm += 1
            elif i[0] < x and i[1] > y:
                mp += 1
            elif i[0] > x and i[1] < y:
                pm += 1
            elif i[0] > x and i[1] > y:
                pp += 1
        M = max(pp, mp, mm, pm)
        min_m = min(min_m, M)

print(min_m)
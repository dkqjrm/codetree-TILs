n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]


check = False
for x in range(1, 101):
    cnt = 0
    for i in array:
        if i[0] <= x and x <= i[1]:
            cnt += 1
    if cnt == n:
        check = True
        print("Yes")
        break

if check is False:
    print("No")
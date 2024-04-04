x = int(input())

V = 1
location = 1
cnt = 0
check = False

while location <= x:
    # print(location, V)
    if check:
        if V != 1:
            V -= 1
    else:
        if location + int(((V+2)*((V+1)/2))) > x and V - 1 >= 1:
            check = True
            V -= 1
        else:
            V += 1
    location += V
    cnt += 1

print(cnt)

# 1 2 3 = 6 (4*1.5)
# 1 2 3 4 = 10 (5*2)
# 1 2 3 4 5 = 15 (6*2.5)
# 1 2 3 4 3 2 1 = 16
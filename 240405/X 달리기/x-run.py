x = int(input())

V = 1
location = 0
cnt = 0
check = False

while location != x:
    location += V
    
    # print(f'도착 위치 {location}, 현재 속도 {V}')
    if x - location < int((V+1+1)*((V+1)/2)) and V > 1:
        V -= 1
    elif x - location >= int((V+1+1)*((V+1)/2)):
        V += 1

    cnt += 1

# 내가 만약 2에서 5로 가야함, 5-2가 V+1~ [3, 2, 1] 보다 크다면 속도 유지 = int((V+1+1)*((V+1)/2))

print(cnt)

# 1 2 3 = 6 (4*1.5)
# 1 2 3 4 = 10 (5*2)
# 1 2 3 4 5 = 15 (6*2.5)
# 1 2 3 4 3 2 1 = 16
# 1 2 3 2 1 = 9
# 1 2 1 2 1 1 = 8
x = int(input())

V = 1
location = 0
cnt = 0
check = False

while location != x:
    location += V
    
    # print(f'도착 위치 {location}, 현재 속도 {V}')
    # 한칸 올린게 괜찮으면 올리기
    if x - location >= int((V+1+1)*((V+1)/2)):
        V += 1
    # 그대로 괜찮으면 유지하기
    elif x - location >= int((V+1)*((V)/2)):
        V = V
    # 아니면 내리기
    else:
        V -= 1


    cnt += 1

# 내가 만약 2에서 5로 가야함, 5-2가 V+1~ [3, 2, 1] 보다 크다면 속도 유지  x - location < int((V+1+1)*((V+1)/2))

print(cnt)

# 1 2 3 = 6 (4*1.5)
# 1 2 3 4 = 10 (5*2)
# 1 2 3 4 5 = 15 (6*2.5)
# 1 2 3 4 3 2 1 = 16
# 1 2 3 2 1 = 9
# 1 2 1 2 1 1 = 8
# 1 2 2 2 1  = 8

# 1 2 2 1 -> 6

# 유지하는게 있어야하네,,
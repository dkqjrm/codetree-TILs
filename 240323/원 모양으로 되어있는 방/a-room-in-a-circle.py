n = int(input())
array = [int(input()) for _ in range(n)]

all = sum(array)

min_result = 1e9
for i in range(n): # 0번째 방에서 시작한다면
    result = 0
    for j in range(n): # 1~(n-1) 방 사람들이 0번쨰 방까지 걸리는 시간
        if i != j :
            result += array[j] * ((j - i + n) % n)
    min_result = min(min_result, result)

print(min_result)
n, m = map(int, input().split())
array = list(map(int, input().split()))

max_total = 0

for i in range(n): # 첫번쨰 움직임이 시작되는 곳
    next_num = array[i]
    total = 0
    for _ in range(m): # 움직임을 m번 진행
        total += array[next_num - 1]
        next_num = array[next_num - 1]

    max_total = max(total, max_total)

print(max_total)
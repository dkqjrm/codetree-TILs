n = int(input())
work_list = [list(map(int, input().split())) for _ in range(n)]


final_result = 0
for i in range(n):
    array = [0] * 1005
    result = 0
    for j in range(n):
        if i != j:
            for time in range(work_list[j][0], work_list[j][1]):
                array[time] += 1
    for work in array:
        if work >= 1:
            result += 1
    final_result = max(result, final_result)

print(final_result)
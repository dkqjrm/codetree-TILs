n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

def distance(array):
    result = 0
    for idx in range(len(array) - 1):
        result += abs(array[idx + 1][0] - array[idx][0]) + abs(array[idx + 1][1] - array[idx][1])    
    return result

min_result = 1e9
for i in range(1, len(array) - 1):
    cal_array = []
    
    for j in range(len(array)):
        if i != j:
            cal_array.append(array[j])
    min_result = min(min_result, distance(cal_array))

print(min_result)
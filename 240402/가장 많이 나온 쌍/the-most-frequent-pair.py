n, m = map(int, input().split())
array = [sorted(list(map(int, input().split()))) for _ in range(m)]

count_dict = {}
for i in array:
    i = str(i)
    if i not in count_dict.keys():
        count_dict[i] = 1
    else:
        count_dict[i] += 1
print(max(count_dict.values()))
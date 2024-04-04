n = int(input())
array = [input().split() for _ in range(n)]

bidul_dict = {}

cnt = 0

for i in array:
    if i[0] not in bidul_dict.keys():
        bidul_dict[i[0]] = i[1]
    else:
        if bidul_dict[i[0]] != i[1]:
            cnt += 1
            bidul_dict[i[0]] = i[1]

print(cnt)
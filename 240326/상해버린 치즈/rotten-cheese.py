n, m, d, s = map(int, input().split())

pmt_array = [list(map(int, input().split())) for _ in range(d)]

pt_array = [list(map(int, input().split())) for _ in range(s)]


# 1, 2, 4
# 사람이 t초 전에 먹은 치즈는 다 의심 대상임.
inspect_list = []
for pt in pt_array:
    # pt[0]이 pt[1] 전에 먹은 치즈를 찾자.
    for pmt in pmt_array:
        if pmt[0] == pt[0] and pmt[2] < pt[1]:
            inspect_list.append(pmt[1])

inspect_list = set(inspect_list)

suspect_list = []
for pmt in pmt_array:
    if pmt[1] in inspect_list:
        suspect_list.append(pmt[0])

print(len(set(suspect_list)))
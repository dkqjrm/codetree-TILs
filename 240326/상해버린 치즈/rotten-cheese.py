n, m, d, s = map(int, input().split())
pmt_array = [list(map(int, input().split())) for _ in range(d)]
pt_array = [list(map(int, input().split())) for _ in range(s)]


# 치즈는 하나만 상했음 pt에서 각각의 p가 t전에 먹은 치즈의 교집합
final_inspect_list = []
for pt in pt_array:
    inspect_list = []
    for pmt in pmt_array:
        if pt[0] == pmt[0] and pt[1] > pmt[2]:
            inspect_list.append(pmt[1])
    final_inspect_list.append(set(inspect_list))


final_inspect = final_inspect_list[0]
for idx in range(1, len(final_inspect_list)):
    final_inspect = final_inspect & final_inspect_list[idx]

final_inspect = list(final_inspect)
final_result = 0
for inspect in final_inspect:
    suspect_list = []
    for pmt in pmt_array:
        if pmt[1] == inspect:
            suspect_list.append(pmt[0])
    final_result = max(final_result, len(set(suspect_list)))
print(final_result)
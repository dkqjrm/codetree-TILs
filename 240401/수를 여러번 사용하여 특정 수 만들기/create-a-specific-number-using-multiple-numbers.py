a, b, c = map(int, input().split())

max_num = 0
for a_cnt in range(1, (1000//a) + 2):
    for b_cnt in range(1, (1000//b) + 2):
        tmp = a * a_cnt + b * b_cnt
        if tmp <= c:
            max_num = max(tmp, max_num)
        else:
            break

print(max_num)
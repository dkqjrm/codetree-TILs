n = int(input())
a_list = []
for _ in range(n):
    a_list.append(int(input()))

answer = 0
for idx in range(len(a_list)):
    if idx == 0 or (a_list[idx-1] >= a_list[idx]):
        cnt = 1
    else:
        cnt += 1
    answer = max(answer, cnt)

print(answer)
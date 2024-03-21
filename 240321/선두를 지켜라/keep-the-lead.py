n, m = map(int, input().split())

a_list = [0]
b_list = [0]
for _ in range(n):
    v, t = map(int, input().split())
    for time in range(t):
        a_list.append(a_list[-1] + v)

for _ in range(m):
    v, t = map(int, input().split())
    for time in range(t):
        b_list.append(b_list[-1] + v)

winner = None
cnt = 0
for idx in range(len(a_list)):
    if a_list[idx] > b_list[idx]:
        if winner == 'B':
            cnt += 1
        winner = 'A'
    elif a_list[idx] < b_list[idx]:
        if winner == 'A':
            cnt += 1
        winner = 'B'
# print(a_list)
# print(b_list)
print(cnt)
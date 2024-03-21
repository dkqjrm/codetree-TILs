n, m = map(int, input().split())
a_list = [0]
b_list = [0]

for _ in range(n):
    t, d = input().split()
    t = int(t)
    if d == 'L':
        for time in range(t):
            a_list.append(a_list[-1] - 1)
    else:
        for time in range(t):
            a_list.append(a_list[-1] + 1)

for _ in range(m):
    t, d = input().split()
    t = int(t)
    if d == 'L':
        for time in range(t):
            b_list.append(b_list[-1] - 1)
    else:
        for time in range(t):
            b_list.append(b_list[-1] + 1)

if len(a_list) > len(b_list):
    for _ in range(len(a_list) - len(b_list)):
        b_list.append(b_list[-1])
elif len(a_list) < len(b_list):
    for _ in range(len(b_list) - len(a_list)):
        a_list.append(a_list[-1])

cnt = 0
for idx in range(len(a_list)):
    if idx != 0 and a_list[idx - 1] != b_list[idx - 1] and (a_list[idx] == b_list[idx]):
        cnt += 1
    # print(a_list[idx], b_list[idx])
    
print(cnt)
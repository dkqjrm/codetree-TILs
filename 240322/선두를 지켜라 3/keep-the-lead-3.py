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

honor = []
for idx in range(len(a_list)):
    if a_list[idx] > b_list[idx]:
        honor.append('A')
    elif a_list[idx] < b_list[idx]:
        honor.append('B')
    elif a_list[idx] == b_list[idx]:
        honor.append('AB')

result = 0
for i in range(len(honor)):
    if i != 0 and honor[i-1] != honor[i]:
        result += 1

print(result)
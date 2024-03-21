n = int(input())
A_list = []
for _ in range(n):
    A_list.append(int(input()))

ans = 0
for idx in range(len(A_list)):
    if idx == 0 or (A_list[idx-1] * A_list[idx] < 0):
        cnt = 1
    else:
        cnt += 1
    ans = max(ans, cnt)

print(ans)
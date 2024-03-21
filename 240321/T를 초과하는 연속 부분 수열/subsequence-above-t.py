n, t = map(int, input().split())
a_list = list(map(int, input().split()))

ans = 0
for idx in range(n):
    if a_list[idx] <= t:
        cnt = 0
    else:
        cnt += 1
    ans = max(ans, cnt)

print(ans)
n, m = map(int, input().split())
ans = []

def solve(curr_num):
    if curr_num == m + 1:
        print(*ans)

    for num in range(1, n + 1):
        if curr_num == 1 or num > ans[-1]:
            ans.append(num)
            solve(curr_num + 1)
            ans.pop()

solve(1)
n, m = map(int, input().split())
array = list(map(int, input().split()))

# m 개의 숫자를 뽑자..
ans = []
max_num = 0

# def xor(ans):
#     base = ans[0]
#     for idx in range(1, len(ans)):
#         base = base ^ ans[idx]
#     return base


def solve(cnt, xor_num):
    global max_num
    if cnt == m:
        max_num = max(max_num, xor_num)
        return

    for i in array:
        ans.append(i)
        solve(cnt + 1, xor_num ^ i)
        ans.pop()
    

solve(0, 0)
print(max_num)
n, m = map(int, input().split())
array = list(map(int, input().split()))

# m 개의 숫자를 뽑자..
ans = []
max_num = 0


def solve(cnt, xor_num, last_idx):
    global max_num
    if cnt == m:
        max_num = max(max_num, xor_num)
        return

    for idx, i in enumerate(array):
        if idx > last_idx:
            ans.append(i)
            solve(cnt + 1, xor_num ^ i, idx)
            ans.pop()
    
solve(0, 0, -1)
print(max_num)

# 조합으로 바꿔야함..
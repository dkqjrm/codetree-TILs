n, m = map(int, input().split())
array = list(map(int, input().split()))

# m 개의 숫자를 뽑자..
ans = []
max_num = 0

def xor(ans):
    base = int(bin(ans[0])[2:])
    for idx in range(1, len(ans)):
        base = base ^ int(bin(ans[idx])[2:])
    return int(str(base), 2)
        


def solve(cnt):
    global max_num
    if cnt == m:
        max_num = max(max_num, xor(ans))
        return

    for i in array:
        ans.append(i)
        solve(cnt + 1)
        ans.pop()
    

solve(0)
print(max_num)
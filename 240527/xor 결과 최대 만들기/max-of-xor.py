n, m = map(int, input().split())
array = list(map(int, input().split()))

array.sort()
# m 개의 숫자를 뽑자..
ans = []
max_num = 0


def solve(cnt, xor_num):
    global max_num
    if cnt == m:
        max_num = max(max_num, xor_num)
        return

    for i in array:
        if cnt == 0 or i > ans[-1]:
            ans.append(i)
            solve(cnt + 1, xor_num ^ i)
            ans.pop()
    

solve(0, 0)
print(max_num)
x, y = map(int, input().split())

def check(num):
    num = str(num)
    num_cnt = {}
    for i in num:
        if i not in num_cnt:
            num_cnt[i] = 1
        else:
            num_cnt[i] += 1

    if min(num_cnt.values()) == 1 and max(num_cnt.values()) == (len(num) - 1):
        return True
    else:
        return False
        

cnt = 0
for num in range(x, y + 1):
    cnt += check(num)

print(cnt)
x, y = map(int, input().split())

def checking(num):
    num = str(num)
    for i in range(len(num)//2):
        if num[i] != num[len(num) - 1 - i]:
            return False

    return True

cnt = 0
for num in range(x, y + 1):
    if checking(num):
        cnt += 1

print(cnt)
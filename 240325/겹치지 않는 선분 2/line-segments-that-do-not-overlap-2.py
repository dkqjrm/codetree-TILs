n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

result = 0

def checking(ax1, ax2, bx1, bx2):
    if (ax1 < bx1 and ax2 < bx2) or (ax1 > bx1 and ax2 > bx2):
        return True
    else:
        return False

for i in range(n): # i가 다른 선과 닿는지 확인하는 것.
    check = True

    for j in range(n):
        if i != j:
            if not checking(array[i][0], array[i][1], array[j][0], array[j][1]):
                check = False


    if check is True:
        result += 1

print(result)
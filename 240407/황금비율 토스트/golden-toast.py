n, m = map(int, input().split())

array = list(input())
arrow = n

for _ in range(m):
    tmp = input().split()

    if len(tmp) == 1:
        instruction = tmp[0]
    else:
        instruction, alpha = tmp[0], tmp[1]
    
    if instruction == 'L':
        if arrow != 0 :
            arrow -= 1
    elif instruction == 'R':
        if arrow != n:
            arrow += 1
    elif instruction == 'D':
        if arrow != n - 1:
            array.pop(arrow)
            if arrow != 0:
                arrow -= 1

    elif instruction == 'P':
        array = array[:arrow] + [alpha] + array[arrow:]
        arrow += 1

print(''.join(array))
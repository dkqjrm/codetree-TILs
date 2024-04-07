n, m = map(int, input().split())

array = input()
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
        if arrow != len(array):
            arrow += 1
    elif instruction == 'D':
        if arrow != len(array):
            array = array[:arrow] + array[arrow+1:]

    elif instruction == 'P':
        array = array[:arrow] + alpha + array[arrow:]
        arrow += 1
    # print(array, arrow)

print(array)
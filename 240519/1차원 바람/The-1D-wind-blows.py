n, m, q = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(n)]

# 위 하고, 아래 하고.

def wind(matrix, r, d):
    if d == 'L':
        matrix[r] = matrix[r][-1:] + matrix[r][0:-1]
    elif d == 'R':
        matrix[r] = matrix[r][1:] + matrix[r][:1]
    # for i in matrix:
    #     print(*i)
    # print('--')
    return matrix

for _ in range(q):
    r, d = input().split()
    init_d = d
    r = int(r) - 1
    matrix = wind(matrix, r, d)
    
    for i in range(r - 1, -1, -1):
        if any(matrix[i + 1][j] == matrix[i][j] for j in range(m)):
            if d == 'L':
                d = 'R'
            else:
                d = 'L'
            matrix = wind(matrix, i, d)
    
    d = init_d

    for i in range(r + 1, n):
        if any(matrix[i - 1][j] == matrix[i][j] for j in range(m)):
            if d == 'L':
                d = 'R'
            else:
                d = 'L'
            matrix = wind(matrix, i, d)

for i in matrix:
    print(*i)
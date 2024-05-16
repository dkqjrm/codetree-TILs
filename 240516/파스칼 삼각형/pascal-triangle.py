r, c, w = map(int, input().split())

# 파스칼 삼각형을 만들자.. 30크기..

matrix = [[0] * 31 for _ in range(31)]
for i in range(31):
    matrix[i][0] = 1
    matrix[i][-1] = 1

for i in range(1, 31):
    for j in range(1, 30):
        if j != 0:
            matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]

def make_sum(r, c, w):
    total = 0
    for i in range(w + 1):
        for j in range(i):
            total += matrix[r+i][c+j]
    
    return total
    


print(make_sum(r - 2, c - 1, w))

# 꼭지점은 r, c
# 3,2 + 4,2 + 4,3 + 5,2 + 5,3+ 5,4
# 행복한 수열의 개수
# 연속하여 m개 이상의 동일한 원소가 나오는 순간이 존재하는 수열
# n * n 크기의 격자 정보가 주어졌을 때 각 행마다 봤을 때 나오는 n개의 수열과, 각 열마다 봤을 때 나올 수 있는 n개의 수열을 포함하여 총 2n개의 수열 중 행복한 수열의 개수를 세서 출력
# -> 즉 최대 크기는 2n개


# 시작점은 첫 번째 row 또는 첫 번째 column
# [[0, 0], [0, 1], [0, 2]] 또는 [[0, 0], [1, 0], [2, 0]] 과 같음

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
total = 0

for i in range(n):
    tmp = -1
    cnt = 1
    for r in range(n):
        if matrix[r][i] == tmp:
            cnt += 1
        else:
            cnt = 1
            
        if cnt >= m:
            total += 1
            break
        tmp = matrix[r][i]

for i in range(n):
    tmp = -1
    cnt = 1
    for c in range(n):
        if matrix[i][c] == tmp:
            cnt += 1
        else:
            cnt = 1

        if cnt >= m:
            total += 1
            break
        tmp = matrix[i][c]

print(total)
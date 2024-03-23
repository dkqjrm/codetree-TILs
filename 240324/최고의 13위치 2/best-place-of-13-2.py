n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

dr = 0
dc = 1

# def in_range(r, c, n):
#     return 0 <= r and 0 <= c and r < n and c < n

max_result = 0

for i in range(n):
    for j in range(n - 2):
        for k in range(n):
            for l in range(n - 2):
                if (i == k and l > j + 2) or i < k:
                    result = 0
                    for idx in range(3):
                        result += matrix[i+(dr*idx)][j+(dc*idx)]
                        result += matrix[k+(dr*idx)][l+(dc*idx)]
                    max_result = max(max_result, result)

print(max_result)
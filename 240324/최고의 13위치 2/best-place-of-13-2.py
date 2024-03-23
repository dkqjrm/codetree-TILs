n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

dr = 0
dc = 1

def in_range(r, c, n):
    return 0 <= r and 0 <= c and r < n and c < n

max_result = 0

for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if (i == k and l > j + 2) or i < k:
                    cnt = 0
                    result = 0
                    for idx in range(3):
                        if in_range(i+(dr*idx), j+(dc*idx), n):
                            cnt += 1
                            result += matrix[i+(dr*idx)][j+(dc*idx)]

                        if in_range(k+(dr*idx), l+(dc*idx), n):
                            cnt += 1
                            result += matrix[k+(dr*idx)][l+(dc*idx)]

                    if cnt == 6:
                        max_result = max(max_result, result)

print(max_result)
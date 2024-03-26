n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]


cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            tmp_array = [0] * 105
            for l in range(n):
                if l != i and l != j and l != k:
                    for idx in range(array[l][0], array[l][1] + 1):
                        tmp_array[idx] += 1

            if max(tmp_array) <= 1:
                cnt += 1

print(cnt)
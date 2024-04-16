n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * (n + 1)
# 1 ~ n 까지의 순열을 만들고, 각 row에 순열 값을 대입해서 max 값 찾으면 될 듯.

total = 0
answer = []
def find(num):
    global total
    if num == n + 1:
        tmp_total = 0
        for idx, i in enumerate(answer):
            tmp_total += matrix[idx][i]
        # print(answer)
        total = max(tmp_total, total)
        return
    
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            answer.append(i)
            
            find(num + 1)

            answer.pop()
            visited[i] = 0

find(1)
print(total)
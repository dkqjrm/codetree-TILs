n = int(input())
visited = [0] * (n + 1)
answer = []

def choose(curr_num):
    if curr_num == n + 1:
        print(*answer)
        return
    
    for i in range(1, n + 1):
        if visited[i]:
            continue

        visited[i] = 1
        answer.append(i)

        choose(curr_num + 1)

        answer.pop()
        visited[i] = 0

choose(1)
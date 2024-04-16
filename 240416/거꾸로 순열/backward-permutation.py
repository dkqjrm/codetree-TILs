n = int(input())
visited = [0] * (n + 1)
answer = []

def choose(num):
    if num == n + 1:
        print(*answer)
        return
    
    for i in range(n, 0, -1):
        if visited[i] == 0:
            answer.append(i)
            visited[i] = 1

            choose(num+1)
            
            answer.pop()
            visited[i] = 0

choose(1)
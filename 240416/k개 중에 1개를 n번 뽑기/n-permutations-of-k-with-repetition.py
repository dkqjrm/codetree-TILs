k, n = map(int, input().split())

result = []
def choosing(num):
    if num == n + 1:
        print(*result)
        return 
    
    for i in range(1, k+1):
        result.append(i)
        choosing(num + 1)
        result.pop()

choosing(1)
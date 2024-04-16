n = int(input())

possible = ['1', '22', '333', '4444']
results = []
result = ''
def choosing():
    global result
    if len(result) == n:
        # print(result)
        results.append(result[:])
        return 
    
    for p in possible:
        if len(result + p) <= n:
            result += p
            choosing()
            result = result[:-len(p)]
choosing()

print(len(results))
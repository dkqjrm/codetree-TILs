n = int(input())
X = list(map(int, input().split()))

def solve(idx):
    if idx == 0:
        return X[0]
    
    return max(solve(idx - 1), X[idx])

print(solve(len(X) - 1))
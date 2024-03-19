n = int(input())
X = list(map(int, input().split()))

def solve(X, idx):
    if idx == 0:
        return X[0]
    
    return max(solve(X, idx - 1), X[idx])

print(solve(X, len(X) - 1))
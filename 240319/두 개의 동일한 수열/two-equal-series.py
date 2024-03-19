n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def solve(n, A, B):
    A.sort()
    B.sort()
    for idx in range(n):
        if A[idx] != B[idx]:
            return 'No'
        return 'Yes'

print(solve(n, A, B))
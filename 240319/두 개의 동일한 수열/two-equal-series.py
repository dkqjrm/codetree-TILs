n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def solve(A, B):
    A.sort()
    B.sort()
    for idx in range(len(A)):
        if A[idx] != B[idx]:
            return 'No'
        return 'Yes'

print(solve(A, B))
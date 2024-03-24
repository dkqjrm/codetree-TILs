n, m = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

def count_dict(A):
    counts = {}
    for i in A:
        if i not in counts.keys():
            counts[i] = 1
        else:
            counts[i] += 1
    return counts

count_B = count_dict(B)
answer = 0

for i in range(n):
    for j in range(i+1, n+1):
        if count_dict(A[i:j]) == count_B:
            answer += 1

print(answer)
n = int(input())
A_array = list(map(int, input().split()))
B_array = list(map(int, input().split()))

cnt = 0
for idx in range(n-1):
    cnt += A_array[idx] - B_array[idx]
    A_array[idx + 1] += A_array[idx] - B_array[idx]

print(cnt)
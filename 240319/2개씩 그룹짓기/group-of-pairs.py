N = int(input())
A_list = list(map(int, input().split()))

result_list = []

A_list.sort()

for i in range(N):
    result_list.append(A_list[i] + A_list[-i-1])

print(max(result_list))

# 0, 1
# 0, 1
# -1, -2
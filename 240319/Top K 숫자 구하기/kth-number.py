N, k = map(int, input().split())

A_list = list(map(int, input().split()))

A_list.sort()

print(A_list[k-1])
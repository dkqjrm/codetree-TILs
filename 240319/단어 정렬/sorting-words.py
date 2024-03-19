n = int(input())
A_list = []
for _ in range(n):
    A_list.append(input())

A_list.sort()
print('\n'.join(A_list))
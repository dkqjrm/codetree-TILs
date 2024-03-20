n = int(input())

A_list = list(map(int, input().split()))
for idx, tmp in enumerate(A_list):
    
    if tmp % 2 != 0:
        print(A_list[idx//2], end=' ')
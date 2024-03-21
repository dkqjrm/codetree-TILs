n = int(input())
A_list = []
for _ in range(n):
    A_list.append(input())

result = []
for i in range(len(A_list)):
    if i == 0 or (A_list[i-1] != A_list[i]):
        cnt = 1
    else:
        cnt += 1
    result.append(cnt)
    
print(max(result))
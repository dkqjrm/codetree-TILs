n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]

check = False

for idx in range(n):
    min_x2 = 1e12
    max_x1 = 0
    for i in array[:idx] + array[idx+1:]: # x2의 min 값이 x1의 맥스값보다 크거나 같으면 됨
        min_x2 = min(min_x2, i[1])
        max_x1 = max(max_x1, i[0])
    if min_x2 >= max_x1:
        check = True
        
    
if check:
    print("Yes")
else:
    print("No")
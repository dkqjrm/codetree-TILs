n = int(input())
array = [list(map(int, input().split())) for _ in range(n)]


# check = False
# for x in range(1, 101):
#     cnt = 0
#     for i in array:
#         if i[0] <= x and x <= i[1]:
#             cnt += 1
#     if cnt == n:
#         check = True
#         print("Yes")
#         break

# if check is False:
#     print("No")
    
max_x1 = 0
min_x2 = 1e12
for i in array:
    max_x1 = max(max_x1, i[0])
    min_x2 = min(min_x2, i[1])

if min_x2 >= max_x1:
    print("Yes")
else:
    print("No")
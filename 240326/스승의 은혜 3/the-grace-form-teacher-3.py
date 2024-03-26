# n, b = map(int, input().split())

# array = [list(map(int, input().split())) for _ in range(n)]


# max_cnt = 0
# for i in range(n):
#     array[i][0] //= 2
#     cnt = 0
#     price = 0
#     for student in sorted(array, key = lambda x : x[0] + x[1]):
#         if price + student[0] + student[1] <= b:
#             cnt += 1
#             price += student[0] + student[1]
#     max_cnt = max(max_cnt, cnt)
#     array[i][0] *= 2

# print(max_cnt)
    
n, b = map(int, input('').split(' '))
pre = []
for i in range(n):
    pre.append(list(map(int, input('').split(' '))))
pre.sort()

cnt = 0
s = 0

for i in range(n):
    price = pre[i][0] + pre[i][1]
    if s + price <= b: # 예산 미초과
       s += price
       cnt += 1
    else : # 예산 초과
        if s + (pre[i][0]/ 2)+ pre[i][1] <= b: # 쿠폰 쓰면 safe
            cnt += 1
            break
print(cnt)
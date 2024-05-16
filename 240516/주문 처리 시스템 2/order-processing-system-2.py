from itertools import permutations

# n, m = map(int, input().split()) # n개의 주문, m개의 처리기
# array = list(map(int, input().split())) # 처리기 용량


# # dp로 풀자

# dp = [1e12] * (n + 1)
# dp[0] = 0

# # 1 1 2면 1 2 3이 가능한거 아님?
# # for i in range(m):
# #     for j in range(m):
# #         if i != j and array[i] + array[j] not in array:
# #             array.append(array[i] + array[j])
# #[1, 1, 1, 1, 2, 2, 2, 3]

# for i in permutations(array, 2):
#     if sum(i) not in array:
#         array.append(sum(i))

# for current_num in range(n + 1): # 다 한번씩 처리할 수 있는 양으로 볼거임.
#     for i in array:
#         if current_num + i <= n:
#             dp[current_num + i] = min(dp[current_num] + 1, dp[current_num + i])

# if dp[n] != 1e12:
#     print(dp[n])
# else:
#     print(-1)
    
# print(dp)

n, m = map(int, input().split()) # n개의 주문, m개의 처리기
array = list(map(int, input().split())) # 처리기 용량

# # 1 1 2면 1 2 3이 가능한거 아님?
# for i in range(m):
#     for j in range(m):
#         if i != j and array[i] + array[j] not in array:
#             array.append(array[i] + array[j])
# #[1, 1, 1, 1, 2, 2, 2, 3]

for i in permutations(array, 2):
    if sum(i) not in array:
        array.append(sum(i))

dp = [1e12] * (max(array) * 2 + 1)
dp[0] = 0


for current_num in range(max(array) * 2): # 다 한번씩 처리할 수 있는 양으로 볼거임.
    for i in array:
        if current_num + i <= max(array) * 2:
            dp[current_num + i] = min(dp[current_num] + 1, dp[current_num + i])

# print(n % max(array))
# print(dp)
if dp[n % max(array) + max(array)] + n // max(array) - 1 != 1e12:
    print(dp[n % max(array) + max(array)] + n // max(array) - 1)
else:
    print(-1)
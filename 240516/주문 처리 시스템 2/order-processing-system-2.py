from itertools import combinations

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

# for i in combinations(array, 2):
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

# n, m = map(int, input().split()) # n개의 주문, m개의 처리기
# array = list(map(int, input().split())) # 처리기 용량

# for i in combinations(array, 2):
#     if sum(i) not in array:
#         array.append(sum(i))

# dp = [1e12] * (max(array) * 2 + 1)
# dp[0] = 0


# for current_num in range(max(array) * 2): # 다 한번씩 처리할 수 있는 양으로 볼거임.
#     for i in array:
#         if current_num + i <= max(array) * 2:
#             dp[current_num + i] = min(dp[current_num] + 1, dp[current_num + i])

# # print(n % max(array))
# # print(dp)
# if dp[n % max(array) + max(array)] + n // max(array) - 1 != 1e12:
#     print(dp[n % max(array) + max(array)] + n // max(array) - 1)
# else:
#     print(-1)

from itertools import combinations

n, m = map(int, input().split())  # n개의 주문, m개의 처리기
array = list(map(int, input().split()))  # 처리기 용량

# 중복을 방지하여 새로운 배열 생성
unique_sums = set(array)

# 모든 두 원소 조합을 계산하고 그 합을 unique_sums에 추가
for i in combinations(array, 2):
    unique_sums.add(sum(i))

# 중복을 제거한 리스트로 변환
unique_sums = list(unique_sums)

# DP 배열 초기화 (필요한 범위만큼)
max_capacity = max(unique_sums)
dp = [1e12] * (max_capacity * 2 + 1)
dp[0] = 0

# DP 배열 업데이트
for current_num in range(max_capacity * 2 + 1):
    for i in unique_sums:
        if current_num + i <= max_capacity * 2:
            dp[current_num + i] = min(dp[current_num] + 1, dp[current_num + i])

# 결과 계산 및 출력
required_sum = n % max_capacity + max_capacity
result = dp[required_sum] + n // max_capacity - 1

if result != 1e12:
    print(result)
else:
    print(-1)
# a, b, c = map(int, input().split())

# max_num = 0
# for a_cnt in range(0, (1000//a) + 1):
#     for b_cnt in range(0, (1000//b) + 1):
#         tmp = a * a_cnt + b * b_cnt
#         if tmp <= c:
#             max_num = max(tmp, max_num)
#         else:
#             break


# 변수 선언 및 입력
a, b, c = map(int, input().split())

max_num = 0

# a를 몇 회 사용할지 전부 시도해 봅니다.
# 모든 경우의 수에 대해 최대가 되도록 하는 수를 계산합니다.
for i in range(c // a + 1):
    # a를 i회 사용합니다.
    cnt = a * i

    # 값을 최대로 하기 위해 b를 몇회 사용해야 하는지 계산합니다.
    num_b = (c - cnt) // b

    cnt += num_b * b
    
    max_num = max(max_num, cnt)

print(max_num)
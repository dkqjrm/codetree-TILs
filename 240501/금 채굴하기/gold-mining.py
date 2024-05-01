# n x n크기의 이차원 영역에 파묻힌 금을 손해를 보지 않는 선에서 최대한 많이 채굴.
# 채굴은 마름모 모양으로 한번만 가능함.
# 마름모 모양이란 특정 중심점을 기준으로 K번 이내로 상하좌우의 인접한 곳으로 이동하는 것을 반복했을 떄 갈 수 있는 모든 영역
# 채굴에 드는 비용은 마름모 안의 격자 갯수만큼 들어가며 K * K + (K + 1)*(K + 1)로 계산 가능 함.
# 손해를 보지 않으면서 채굴할 수 있는 가장 많은 금의 개수

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

max_total = 0

def solve(r, c, k):
    total = 0
    for i in range(n):
        for j in range(n):
            if abs(r - i) + abs(c - j) <= k:
                total += matrix[i][j]
    return total

for r in range(n):
    for c in range(n):
        for k in range(n - 1):
            cost = (k ** 2 + (k + 1) ** 2)
            total = solve(r, c, k)
            if (total * m) - cost >= 0:
                max_total = max(max_total, total)

print(max_total)
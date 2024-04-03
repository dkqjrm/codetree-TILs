n = int(input())
array = [int(input()) for _ in range(n)]

# 최소, 최대 값을 정해두면 되는거 아님?

min_cost = 1e12
for mini in range(min(array), max(array)):
    maxi = mini + 17

    cost = 0
    for num in array:
        if num < mini:
            cost += (mini - num) ** 2
        elif num > maxi:
            cost += (num - maxi) ** 2
    min_cost = min(cost, min_cost)

print(min_cost)
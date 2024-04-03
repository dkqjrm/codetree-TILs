n, k = map(int, input().split())
array = list(map(int, input().split()))

min_cost = 1e12

for mini in range(min(array), max(array) + 1):
    maxi = mini + 2
    cost = 0

    for i in array:
        if i < mini:
            cost += mini - i
        elif maxi < i:
            cost += i - maxi

    min_cost = min(cost, min_cost)

print(min_cost)
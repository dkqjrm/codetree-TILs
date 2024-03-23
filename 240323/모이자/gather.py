n = int(input())
people = list(map(int, input().split()))

min_result = 1e9

for idx in range(n):
    result = 0
    for j in range(n):
        if idx != j:
            result += people[j] * abs(j - idx)

    if min_result > result:
        min_result = result

print(min_result)
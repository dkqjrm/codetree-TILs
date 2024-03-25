array = list(map(int, input().split()))

total = sum(array)

result = 1e9

for i in range(len(array)):
    for j in range(i+1, len(array)):
        for k in range(len(array)):
            if k != i and k != j:
                for l in range(k+1, len(array)):
                    if l != j and l != i:
                        team1 = array[i] + array[j]
                        team2 = array[k] + array[l]
                        team3 = total - team1 - team2
                        result = min(result, max(team1, team2, team3) - min(team1, team2, team3))

print(result)
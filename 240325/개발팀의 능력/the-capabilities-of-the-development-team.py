array = list(map(int, input().split()))

total = sum(array)

result = 1e9

for i in range(len(array)):
    for j in range(i+1, len(array)):
        for k in range(len(array)):
            if k != i and k != j:
                for l in range(k+1, len(array)):
                    if l != i and l != j:
                        team1 = array[i] + array[j]
                        team2 = array[k] + array[l]
                        team3 = total - team1 - team2
                        if team1 != team2 and team2 != team3 and team1 != team3:
                            result = min(result, max(team1, team2, team3) - min(team1, team2, team3))
                        
if result == 1e9:
    print(-1)
else:
    print(result)
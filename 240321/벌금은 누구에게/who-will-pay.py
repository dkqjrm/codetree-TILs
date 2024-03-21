n, m, k = map(int, input().split())
punishments = [0 for _ in range(n)]


check = False
for _ in range(m):
    person = int(input())
    punishments[person - 1] += 1
    if punishments[person - 1] >= k:
        print(person)
        check = True
        break
if check == False:
    print(-1)
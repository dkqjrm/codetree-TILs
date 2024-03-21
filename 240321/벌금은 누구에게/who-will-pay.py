n, m, k = map(int, input().split())
punishments = []

for _ in range(n):
    punishments.append(0)

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
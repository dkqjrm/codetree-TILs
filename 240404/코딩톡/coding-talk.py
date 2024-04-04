n, m, p = map(int, input().split())
array = [input().split() for _ in range(m)]

# p와 같거나 뒤에 말한 사람들은 다 읽었음.


people = []
for i in range(n):
    people.append(chr(65+i))

for idx, (c, u) in enumerate(array):
    if idx >= (p-1) and c in people:
        people.remove(c)
    if idx == (p-1) and u == 0:
        people = []
print(*people)


# 6 6 1
# D 0
# C 1
# B 2
# B 2
# A 2
# F 4
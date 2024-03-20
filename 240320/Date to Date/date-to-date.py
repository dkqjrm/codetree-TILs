num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

m1, d1, m2, d2 = map(int, input().split())

total = 0
for m in range(m1, m2):
    total += num_of_days[m]

total -= d1
total += d2

print(total)
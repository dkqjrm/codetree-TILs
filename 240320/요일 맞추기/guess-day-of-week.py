m1, d1, m2, d2 = map(int, input().split())

num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_the_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

first_days = 0
for i in range(m1 - 1):
    first_days += num_of_days[i]
first_days += d1

second_days = 0
for i in range(m2 - 1):
    second_days += num_of_days[i]
second_days += d2

print(day_of_the_week[(second_days - first_days) % 7])
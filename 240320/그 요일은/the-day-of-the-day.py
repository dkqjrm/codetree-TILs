m1, d1, m2, d2 = map(int, input().split())
A = input()

num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_the_week = {
    'Mon' : 1,
    'Tue' : 2,
    'Wed' : 3,
    'Thu' : 4,
    'Fri' : 5,
    'Sat' : 6,
    'Sun' : 7}

first_days = 0
for i in range(m1 - 1):
    first_days += num_of_days[i]
first_days += d1

second_days = 0
for i in range(m2 - 1):
    second_days += num_of_days[i]
second_days += d2

print((second_days - first_days) // 7 + 1 + int((second_days - first_days) % 7 >= day_of_the_week[A]))
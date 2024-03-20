n = int(input())
students = []
for idx in range(1, n+1):
    h, w = map(int,input().split())
    students.append((h, w, idx))

students.sort()

for student in students:
    print(*student)
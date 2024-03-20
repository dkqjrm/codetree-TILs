class Student:
    def __init__(self, name, korean, english, math):
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math

    def __str__(self):
        return f'{self.name} {self.korean} {self.english} {self.math}'

n = int(input())

students = []
for _ in range(n):
    tmp = input().split()
    students.append(Student(tmp[0], int(tmp[1]), int(tmp[2]), int(tmp[3])))

students.sort(key = lambda x : (-x.korean, -x.english, -x.math))

for student in students:
    print(student)
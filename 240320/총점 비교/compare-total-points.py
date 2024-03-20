class Student:
    def __init__(self, name, one, two, three):
        self.name = name
        self.one = one
        self.two = two
        self.three = three

    def __str__(self):
        return f'{self.name} {self.one} {self.two} {self.three}'

n = int(input())
students = []

for _ in range(n):
    student = input().split()
    students.append(Student(student[0], int(student[1]), int(student[2]), int(student[3])))

students.sort(key = lambda x : x.one + x.two + x.three)

for student in students:
    print(student)
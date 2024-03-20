class Student:
    def __init__(self, height, weight, idx):
        self.height = height
        self.weight = weight
        self.idx = idx

    def __str__(self):
        return f'{self.height} {self.weight} {self.idx}'

n = int(input())

students = []
for idx in range(1, n+1):
    student = list(map(int, input().split()))
    students.append(Student(student[0], student[1], idx))

students.sort(key = lambda x: (-x.height, -x.weight, x.idx))

for student in students:
    print(student)
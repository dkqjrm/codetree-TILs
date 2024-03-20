class Student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def __str__(self):
        return (f'{self.name} {self.height} {self.weight}')

n = int(input())
students = [Student(*input().split()) for _ in range(n)]

students.sort(key=lambda x: x.height)

for student in students:
    print(student)
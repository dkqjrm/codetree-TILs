class Student:
    def __init__(self, height, weight, idx):
        self.height = height
        self.weight = weight
        self.idx = idx

    def __str__(self):
        return f'{self.height} {self.weight} {self.idx}'

n = int(input())

student_list = []
for idx in range(1, n+1):
    h, w = map(int, input().split())
    student_list.append(Student(h, w, idx))

student_list.sort(key = lambda x : (x.height, -x.weight))

for student in student_list:
    print(student)
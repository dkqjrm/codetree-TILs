class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
    
    def __str__(self):
        return f'{self.name} {self.height} {self.weight}'

n = int(input())

people = []
for _ in range(n):
    name, height, weight = input().split()
    height, weight = map(int, (height, weight))

    people.append(Person(name, height, weight))

people.sort(key = lambda x : (x.height, -x.weight))

for person in people:
    print(person)
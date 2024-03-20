class Person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def __str__(self):
        return '{} {:.0f} {:.1f}'.format(self.name, self.height, self.weight)

people = []
for _ in range(5):
    name, height, weight = input().split()
    height, weight = map(float, (height, weight))

    people.append(Person(name, height, weight))

people.sort(key = lambda x : x.name)
print('name')
for person in people:
    print(person)

print()

people.sort(key = lambda x : -x.height)
print('height')
for person in people:
    print(person)
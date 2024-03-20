class Test:
    def __init__(self, id='codetree', level='10'):
        self.id = id
        self.level = level

    def __str__(self):
        return(f'user {self.id} lv {self.level}')

class_test = Test()
print(class_test)

tmp = input().split()
class_test.id = tmp[0]
class_test.level = tmp[1]

print(class_test)
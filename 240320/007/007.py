class test:
    def __init__(self, code, location, time):
        self.code = code
        self.location = location
        self.time = time

    def __str__(self):
        return (f'''secret code : {self.code}
meeting point : {self.location}
time : {self.time}''')

tmp = input().split()
class_test = test(*tmp)
print(class_test)
n = int(input())

class Stack():
    def __init__(self):
        self.arr = []

    def push(self, A):
        self.arr.append(A)
    
    def pop(self):
        if len(self.arr) >= 1:
            print(self.arr.pop())
    
    def size(self):
        print(len(self.arr))

    def empty(self):
        if len(self.arr):
            print(0)
        else:
            print(1)

    def top(self):
        print(self.arr[-1])

stack = Stack()

for _ in range(n):
    instruction = input().split()

    if len(instruction) == 1 :
        instruction = instruction[0]
    else:
        num = int(instruction[1])
        instruction = instruction[0]
        
    
    if instruction == 'push':
        stack.push(num)
    elif instruction == 'pop':
        stack.pop()
    elif instruction == 'size':
        stack.size()
    elif instruction == 'empty':
        stack.empty()
    elif instruction == 'top':
        stack.top()
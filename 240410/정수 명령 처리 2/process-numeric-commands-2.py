from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()
        
    def push(self, item):
        self.dq.append(item)
    
    def empty(self):
        return not self.dq

    def size(self):
        return len(self.dq)

    def pop(self):
        if not self.empty():
            return self.dq.popleft()
    
    def front(self):
        if not self.empty():
            return self.dq[0]
    

n = int(input())
queue = Queue()

for _ in range(n):
    instruction = input().split()

    if len(instruction) == 1:
        instruction = instruction[0]
    
    else:
        item = instruction[1]
        instruction = instruction[0]

    if instruction == 'push':
        queue.push(item)
    elif instruction == 'pop':
        print(queue.pop())
    elif instruction == 'size':
        print(queue.size())
    elif instruction == 'empty':
        print(int(queue.empty()))
    elif instruction == 'front':
        print(queue.front())
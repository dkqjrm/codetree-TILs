from collections import deque

n, k = map(int, input().split())

class Queue():
    def __init__(self):
        self.queue = deque()
        
    def push(self, item):
        self.queue.append(item)

    def pop(self):
        return self.queue.popleft()
    
    def top(self):
        return self.queue.topleft()

    def size(self):
        return len(self.queue)
    
    def empty(self):
        return not self.queue
    

queue = Queue()

for i in range(1, n+1):
    queue.push(i)

while not queue.empty():
    for _ in range(k-1):
        queue.push(queue.pop())

    print(queue.pop(), end=' ')
from collections import deque

dq = deque()

n = int(input())

for _ in range(n):
    instruction = input().split()
    if len(instruction) == 1:
        instruction = instruction[0]
    
    else:
        num = instruction[1]
        instruction = instruction[0]

    if instruction == 'push_front':
        dq.appendleft(num)
    elif instruction == 'push_back':
        dq.append(num)
    elif instruction == 'pop_front':
        print(dq.popleft())
    elif instruction == 'pop_back':
        print(dq.pop())
    elif instruction == 'size':
        print(len(dq))
    elif instruction == 'empty':
        print(int(not dq))
    elif instruction == 'front':
        print(dq[0])
    elif instruction == 'back':
        print(dq[-1])
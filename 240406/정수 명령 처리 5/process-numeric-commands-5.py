n = int(input())
array = []

for _ in range(n):
    instruction = input().split()
    if len(instruction) == 2:
        num = int(instruction[1])
        instruction = instruction[0]

    if instruction == 'push_back':
        array.append(num)
    elif instruction[0] == 'pop_back':
        array.pop()
    elif instruction[0] == 'size':
        print(len(array))
    elif instruction == 'get':
        print(array[num - 1])
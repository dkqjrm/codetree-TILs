array = input()

result = 0

for i in range(len(array)):
    if array[i] == '(':
        for j in range(i, len(array)):
            if array[j] == ')':
                result += 1

print(result)
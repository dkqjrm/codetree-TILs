n = int(input())
array = input()

result = 0

for i in range(n):
    if array[i] == 'C':
        for j in range(i+1, n):
            if array[j] == 'O':
                for k in range(j+1, n):
                    if array[k] == 'W':
                        result += 1
print(result)
array = input()

length = len(array)
result = 0

for i in range(length-3):
    if array[i:i+2] == '((':
        for j in range(i + 2, length-1):
            if array[j:j+2] == '))':

                result += 1



print(result)
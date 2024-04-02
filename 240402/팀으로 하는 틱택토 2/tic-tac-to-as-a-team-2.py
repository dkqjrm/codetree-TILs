array = [list(map(int, list(input()))) for _ in range(3)]

result = []
for i in array:
    if len(set(i)) == 2:
        result.append(set(i))

# print(array)

if len(set([array[0][0], array[1][0], array[2][0]])) == 2 and set([array[0][0], array[1][0], array[2][0]]) not in result:
    result.append(set([array[0][0], array[1][0], array[2][0]]))
if len(set([array[0][1], array[1][1], array[2][1]])) == 2 and set([array[0][1], array[1][1], array[2][1]]) not in result:
    result.append(set([array[0][1], array[1][1], array[2][1]]))
if len(set([array[0][2], array[1][2], array[2][2]])) == 2 and set([array[0][2], array[1][2], array[2][2]]) not in result:
    result.append(set([array[0][2], array[1][2], array[2][2]]))

if len(set([array[0][0], array[1][1], array[2][2]])) == 2 and set([array[0][0], array[1][1], array[2][2]]) not in result:
    result.append(set([array[0][0], array[1][1], array[2][2]]))
if len(set([array[0][2], array[1][1], array[2][0]])) == 2 and set([array[0][2], array[1][1], array[2][0]]) not in result:
    result.append(set([array[0][2], array[1][1], array[2][0]]))

print(len(result))
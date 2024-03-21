OFFSET = 200

n = int(input())

visited = [('Blank', 0, 0)] * 400

def move(location, x, arrow):
    x = int(x)
    if arrow == 'L':
        new_location = location - x
        for i in range(new_location, location):
            visited[i] = (0, visited[i][1] + 1, visited[i][2])
            if visited[i][1] >= 2 and visited[i][2] >= 2:
                visited[i] = (2, visited[i][1], visited[i][2])
            
    else:
        new_location = location + x
        for i in range(location, new_location):
            visited[i] = (1, visited[i][1], visited[i][2] + 1)
            if visited[i][1] >= 2 and visited[i][2] >= 2:
                visited[i] = (2, visited[i][1], visited[i][2])
            
    return new_location

location = OFFSET
for _ in range(n):
    x, arrow = input().split()
    location = move(location, x, arrow)

white = 0
black = 0
grey = 0
for i in visited:
    if i[0] == 0:
        white += 1
    elif i[0] == 1:
        black += 1
    elif i[0] == 2:
        grey += 1

# print(visited)
print(f'{white} {black} {grey}')

#     200 201 202 203
# 199 200 201 202 203
# 199 200 201 202 203 204 205
#             202 203 204 205
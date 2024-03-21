OFFSET = 150000

n = int(input())
# n = 5

visited = [('BLANK', 0, 0)] * 300000

# def move(location, x, arrow):
#     x = int(x)
#     if x == 1:
#     if arrow == 'L':
#         new_location = location - x
#         for i in range(new_location, location):
#             visited[i] = (0, visited[i][1] + 1, visited[i][2])
#             if visited[i][1] >= 2 and visited[i][2] >= 2:
#                 visited[i] = (2, visited[i][1], visited[i][2])
            
#     else:
#         if x == 1:
#             x = 0
#         new_location = location + x
#         for i in range(location, new_location):
#             visited[i] = (1, visited[i][1], visited[i][2] + 1)
#             if visited[i][1] >= 2 and visited[i][2] >= 2:
#                 visited[i] = (2, visited[i][1], visited[i][2])
#     return new_location

def move(location, x, arrow):
    x = int(x)
    if arrow == 'L':
        visited[location] = (0, visited[location][1] + 1, visited[location][2])
        if visited[location][1] >= 2 and visited[location][2] >= 2:
            visited[location] = (2, visited[location][1], visited[location][2])
        for _ in range(1,x):
            location -= 1
            visited[location] = (0, visited[location][1] + 1, visited[location][2])
            if visited[location][1] >= 2 and visited[location][2] >= 2:
                visited[location] = (2, visited[location][1], visited[location][2])
    else:
        visited[location] = (1, visited[location][1], visited[location][2] + 1)
        if visited[location][1] >= 2 and visited[location][2] >= 2:
            visited[location] = (2, visited[location][1], visited[location][2])
        for _ in range(1,x):
            location += 1
            visited[location] = (1, visited[location][1], visited[location][2] + 1)
            if visited[location][1] >= 2 and visited[location][2] >= 2:
                visited[location] = (2, visited[location][1], visited[location][2])
    return location

location = OFFSET
for _ in range(n):
    x, arrow = input().split()
    location = move(location, x, arrow)
# for i in [[1,'L'],[1,'L'],[1,'R'],[2,'R'],[1,'L']]:
#     x, arrow = i
#     location = move(location, x, arrow)
    # print(visited[198:202])

white = sum(1 for i in visited if i[0] == 0)
black = sum(1 for i in visited if i[0] == 1)
grey = sum(1 for i in visited if i[0] == 2)


print(f'{white} {black} {grey}')

#     200 201 202 203
# 199 200 201 202 203
# 199 200 201 202 203 204 205
#             202 203 204 205

# 5
# 1 L
# 1 L
# 1 R
# 2 R
# 1 L
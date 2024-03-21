OFFSET = 1005

a_x1, a_y1, a_x2, a_y2 = map(int, input().split())
b_x1, b_y1, b_x2, b_y2 = map(int, input().split())
m_x1, m_y1, m_x2, m_y2 = map(int, input().split())

a_x1, a_y1, a_x2, a_y2 = a_x1 + OFFSET, a_y1 + OFFSET, a_x2 + OFFSET, a_y2 + OFFSET
b_x1, b_y1, b_x2, b_y2 = b_x1 + OFFSET, b_y1 + OFFSET, b_x2 + OFFSET, b_y2 + OFFSET
m_x1, m_y1, m_x2, m_y2 = m_x1 + OFFSET, m_y1 + OFFSET, m_x2 + OFFSET, m_y2 + OFFSET

visited = [[0] * (OFFSET * 2) for _ in range(OFFSET * 2)]

result = 0
for i in range(a_x1, a_x2):
    for j in range(a_y1, a_y2):
        visited[i][j] = 1
        result += 1

for i in range(b_x1, b_x2):
    for j in range(b_y1, b_y2):
        visited[i][j] = 2
        result += 1
    

for i in range(m_x1, m_x2):
    for j in range(m_y1, m_y2):
        if visited[i][j] == 1 or visited[i][j] == 2:
            result -= 1
            
print(result)
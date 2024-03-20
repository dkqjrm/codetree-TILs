class Dot:
    def __init__(self, x, y, idx):
        self.x = x
        self.y = y
        self.idx = idx
    
    def __str__(self):
        return f'{self.idx}'


n = int(input())
dot_list = []
for idx in range(1, n + 1):
    x, y = map(int, input().split())
    dot_list.append(Dot(x, y, idx))

dot_list.sort(key = lambda x : (abs(0 - x.x) + abs(0 - x.y)))

for dot in dot_list:
    print(dot)
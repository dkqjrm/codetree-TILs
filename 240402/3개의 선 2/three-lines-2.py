n = int(input())

array = [list(map(int, input().split())) for _ in range(n)]

def checking(array):
    x_list = []
    y_list = []
    for i in array:
        x_list.append(i[0])
        y_list.append(i[1])
    if len(x_list) <= 3 or len(y_list) <= 3:
        return 1
    else:
        for x in x_list:
            for y1 in y_list:
                for y2 in y_list:
                    if y1 != y2:
                        visited = [0] * (n+1)
                        for idx, i in enumerate(array):
                            if i[0] == x or i[1] == y1 or i[1] == y2:
                                visited[idx] = 1
                        
                        if sum(visited) == n:
                            return 1

        for y in y_list:
            for x1 in x_list:
                for x2 in x_list:
                    if x1 != x2:
                        visited = [0] * (n+1)
                        for idx, i in enumerate(array):
                            if i[0] == x1 or i[0] == x2 or i[1] == y2:
                                visited[idx] = 1
                        
                        if sum(visited) == n:
                            return 1

        return 0



print(checking(array))
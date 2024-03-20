n = int(input())

w_list = [tuple(input().split()) for _ in range(n)]

w_list.sort()

for w in w_list:
    if w[2] == 'Rain':
        print(f'{w[0]} {w[1]} {w[2]}')
        break
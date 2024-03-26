T, a, b = map(int, input().split())
array = [0] * 1005

for _ in range(T):
    alpha, location = input().split()
    location = int(location)
    array[location] = alpha

cnt = 0
for k in range(a, b + 1):
    length_S = 1e9
    length_N = 1e9
    for i in range(a, b + 1):
        if array[i] == 'S':
            length_S = min(length_S, abs(k - i))
        elif array[i] == 'N':
            length_N = min(length_N, abs(k - i))

    if length_S <= length_N:
        cnt += 1

    
print(cnt)
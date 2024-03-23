n, k = map(int, input().split())
array = [0] * (10001)

for i in range(n):
    location, picture = input().split()
    location = int(location)
    if picture == 'G':
        picture = 1
    else:
        picture = 2

    array[location] = picture

max_result = 0
for idx in range(len(array) - k + 1):
    max_result = max(sum(array[idx:idx+k+1]), max_result)

print(max_result)
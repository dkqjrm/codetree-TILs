n = int(input())
array = list(map(int, input().split()))

for i in range(100, -1, -10):
    number = sum([i + 10 > num >= i for num in array])
    if number != 0:
        print("{} - {}".format(i, number))
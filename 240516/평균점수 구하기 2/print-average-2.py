n = int(input())
array = list(map(float, input().split()))

print("{:.1f}".format(sum(array) / n))
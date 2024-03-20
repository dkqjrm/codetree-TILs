n, k, T = input().split()

n, k = int(n), int(k)

words = []

for _ in range(n):
    words.append(input())

words = [word for word in words if word.startswith(T)]

words.sort()

print(words[k-1])
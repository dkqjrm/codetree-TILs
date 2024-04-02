n = int(input())
string = input()


length = 0

for i in range(0, n):
    for start in range(0, n - i):
        refer = string[start:start + i + 1]
        for check in range(0, n - i):
            if start != check:
                if string[check:check + i + 1] == refer:
                    length = i

print(length + 2)
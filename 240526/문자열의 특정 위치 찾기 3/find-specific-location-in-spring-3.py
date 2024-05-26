a = input()
b = input()

def solve(a, b):
    for idx, char in enumerate(a):
        if char == b:
            return idx + 1

    return 'Not Found'

print(solve(a, b))
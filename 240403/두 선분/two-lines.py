x1, x2, x3, x4 = map(int, input().split())

def solve(x1, x2, x3, x4):
    if x2 < x3 or x4 < x1:
        return "nonintersecting"
    else:
        return "intersecting"

print(solve(x1, x2, x3, x4))
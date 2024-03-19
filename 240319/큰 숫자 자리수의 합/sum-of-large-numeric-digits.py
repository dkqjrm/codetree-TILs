x, y, z = map(int, input().split())

xyz = x * y * z

def solve(xyz):
    if xyz < 10:
        return xyz

    return solve(xyz // 10) + xyz % 10

print(solve(xyz))
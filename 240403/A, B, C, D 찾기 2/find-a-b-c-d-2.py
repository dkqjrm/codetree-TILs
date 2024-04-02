array = list(map(int, input().split()))
array.sort()

for A in range(len(array)):
    for B in range(A, len(array)):
        for C in range(B, len(array)):
            for D in range(C, len(array)):
                check_array = [A, B, C, D, A + B, B + C, C + D, D + A, A + C, B + D, A + B + C, A + B + D, A + C + D, B + C + D, A + B + C + D]
                if sorted(check_array) == array:
                    print(A, B, C, D)
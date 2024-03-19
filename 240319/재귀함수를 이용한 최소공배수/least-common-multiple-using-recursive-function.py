n = int(input())
A = list(map(int, input().split()))

# 2개씩 최소 공배수를 비교하고, 나오면 오른쪽꺼랑 비교하면 될 것 같음.
def solve(result, n):
    if n < 0:
        return result

    tmp_a, tmp_b = result, A[n]
    while tmp_b != 0:
        r = tmp_a % tmp_b
        tmp_a = tmp_b
        tmp_b = r
    result = (result * A[n]) // tmp_a

    return solve(result, n-1)


print(solve(1, n-1))
    
    


# lcm(lcm(A[2], A[1]), A[0])
# lcm(n, n-1) -> n과 n-1의 최소공배수
# lcm(lcm(n, n-1), n-2) n과 n-1와 n-2의 최소공배수

# -> n-1과 n-2의 최소 공배수를 return 하고, 그 값과 n-3의 값을 return 하면 됨.
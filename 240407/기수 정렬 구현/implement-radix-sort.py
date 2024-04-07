MAX_K = 6
MAX_DIGIT = 10

n = int(input())
array = list(map(int, input().split()))

def custom_sort(array):
    p = 1
    for pos in range(MAX_K):
        arr_new = [[] for _ in range(MAX_DIGIT)]
        for i in array:
            digit = (i // p) % 10
            arr_new[digit].append(i)

        array = []
        for digit in range(MAX_DIGIT):
            for i in arr_new[digit]:
                array.append(i)

        p *= 10

    return array
    
array = custom_sort(array)

print(*array)
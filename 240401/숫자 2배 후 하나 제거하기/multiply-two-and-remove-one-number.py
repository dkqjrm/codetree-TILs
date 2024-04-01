n = int(input())

array = list(map(int, input().split()))

min_total = 1e12
for idx in range(len(array)):
    array[idx] *= 2
    for delete_idx in range(len(array)):
        tmp_arr = []
        total = 0
        for i, num in enumerate(array):
            if delete_idx != i:
                tmp_arr.append(num)

        for i in range(1, len(tmp_arr)):
            total += (abs(tmp_arr[i] - tmp_arr[i-1]))
        min_total = min(total, min_total)
    array[idx] //= 2

print(min_total)
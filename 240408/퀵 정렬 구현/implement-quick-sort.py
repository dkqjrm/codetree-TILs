n = int(input())
arr = list(map(int, input().split()))

def partition(arr, low, high):
    pivot = arr[high] # 맨 오른쪽 값을 pivot으로 사용
    i = low - 1 # low 보다 아래 값에서 시작

    for j in range(low, high + 1):
        if arr[j] < pivot: # 만약 지금 살펴보고 있는 값이 pivot 보다 작다면,
            i += 1 
            arr[i], arr[j] = arr[j], arr[i] # 큰 값과 교체

    i += 1
    arr[i], arr[j] = arr[j], arr[i] # 피봇과 큰 값과 교체

    return i

def quick_sort(arr, low, high):
    if low < high:
        pos = partition(arr, low, high)

        quick_sort(arr, low, pos - 1)
        quick_sort(arr, pos + 1, high)

quick_sort(arr, 0, len(arr) - 1)

print(*arr)
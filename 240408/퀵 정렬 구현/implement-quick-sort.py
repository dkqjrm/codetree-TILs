n = int(input())
arr = list(map(int, input().split()))

def partition(low, high):
    pivot = arr[high] # 맨 오른쪽 값을 pivot으로 사용
    i = low - 1 # low 보다 아래 값에서 시작

    for j in range(low, high):
        if arr[j] < pivot: # 만약 지금 살펴보고 있는 값이 pivot 보다 작다면,
            i += 1 
            arr[i], arr[j] = arr[j], arr[i] # 큰 값과 교체

    i += 1
    arr[i], arr[high] = arr[high], arr[i] # 피봇과 큰 값과 교체

    return i

def quick_sort(low, high):
    if low < high:
        pos = partition(low, high)

        quick_sort(low, pos - 1)
        quick_sort(pos + 1, high)

quick_sort(0, n - 1)

print(*arr)
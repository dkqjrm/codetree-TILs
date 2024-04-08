n = int(input())
arr = list(map(int, input().split()))

def heapify(n, i):
    largest = i 
    l = i * 2
    r = i * 2 + 1

    if l <= n and arr[l] > arr[largest]:
        largest = l
    if r <= n and arr[r] > arr[largest]:
        largest = r

    if largest != i :
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(n, largest)


def heap_sort(n):
    for i in range(n // 2, -1, -1):
        heapify(n, i) # max-heap 상태로 변환하는것

    for i in range(n, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(i - 1, 0)

heap_sort(n - 1)

print(*arr)
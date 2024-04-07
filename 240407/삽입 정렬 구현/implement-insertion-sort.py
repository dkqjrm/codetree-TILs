n = int(input())
array = list(map(int, input().split()))

def insertion_sort(arr):
  for i in range(n):
    j = i - 1
    key = arr[i]
    while j >= 0 and arr[j] > key: # 지금 조사하고 있는 j가 넣으려는 key 보다 크다면
      arr[j + 1] = arr[j] # j의 뒤와 j를 변경해서 한칸씩 이동.
      j -= 1
    arr[j + 1] = key # 지금 조사하고 있는 j가 넣으려는 key보다 작다면 변경.
  return arr

array = insertion_sort(array)
print(*array)
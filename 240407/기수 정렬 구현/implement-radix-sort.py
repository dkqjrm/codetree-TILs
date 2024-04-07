n = int(input())
array = list(map(int, input().split()))

def custom_sort(array):
    p = 1
    for _ in range(6): # 최대 6자리 숫자까지
        arr_new = [[] for _ in range(10)] # 숫자가 들어갈 리스트 만들기
        for i in array: # 각 숫자를 판단하는거
            digit = (i // p) % 10 # 판단해야하는 자릿수의 수, 만약 없으면 0으로 들어감
            arr_new[digit].append(i)

        array = []
        for digit in range(10):
            for i in arr_new[digit]:
                array.append(i)

        p *= 10

    return array
    
array = custom_sort(array)

print(*array)
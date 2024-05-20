n, m = map(int, input().split())
array = [int(input()) for _ in range(n)]

# n개의 폭탄이 있고, m개 이상 연속으로 같은 숫자가 적혀있는 폭탄들은 터지게 됨.
check = True

while check:
    check = False
    for i in range(len(array) - m + 1):
        if array[i] != None:
            check = i
            while check + 1 < len(array) and array[check + 1] == array[i]:
                check += 1
            if check - i >= m - 1:
                for idx in range(i, check + 1):
                    array[idx] = None
                    check = True

    tmp_array = []
    for i in array:
        if i != None:
            tmp_array.append(i)

    array = tmp_array

print(len(array))
for i in array:
    print(i)
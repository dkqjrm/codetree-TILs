n, k = map(int, input().split())
array = list(map(int, input().split()))

min_result = 1e12

def checking(i):
    possible_index = []
    for idx, num in enumerate(array):
        if num <= i:
            possible_index.append(idx)
    if possible_index[0] > k:
        return False

    for idx in range(1, len(possible_index)):
        if possible_index[idx] - possible_index[idx-1] > k:
            return False
    
    if possible_index[-1] + k < n:
        return False

    return True

for i in range(1, max(array) + 1): # 최댓값이 i 일때
    if checking(i):
        print(i)
        break
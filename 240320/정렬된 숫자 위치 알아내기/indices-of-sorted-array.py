class Number:
    def __init__(self, num, idx, moved_idx=None):
        self.num = num
        self.idx = idx
        self.moved_idx = moved_idx

n = int(input())

A = map(int, input().split())

numbers = [Number(num = num, idx = idx) for idx, num in enumerate(A, start=1)]

numbers.sort(key = lambda x : x.num)

for idx, number in enumerate(numbers, start=1):
    number.moved_idx = idx

numbers.sort(key = lambda x : x.idx)

for number in numbers:
    print(number.moved_idx, end=' ')
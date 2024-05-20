n = int(input()) # 처음 놓여있는 블럭의 수
array = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split()) # s1부터 e1까지의 블럭을 제외
s2, e2 = map(int, input().split()) # s2부터 e2까지의 블럭을 제외

if s1 != 1:
    array = array[:-e1] + array[-s1+1:]
else:
    array = array[:-e1]

if s2 != 1:
    array = array[:-e2] + array[-s2+1:]
else:
    array = array[:-e2]

print(len(array))
for i in array:
    print(i)
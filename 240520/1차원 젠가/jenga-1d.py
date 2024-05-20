n = int(input()) # 처음 놓여있는 블럭의 수
array = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split()) # s1부터 e1까지의 블럭을 제외
s2, e2 = map(int, input().split()) # s2부터 e2까지의 블럭을 제외
tmp_array = []

for i in range(s1 - 1, e1):
    array[i] = None

for i in array:
    if i != None:
        tmp_array.append(i) 
array = tmp_array

tmp_array = []
for i in range(s2 - 1, e2):
    array[i] = None

for i in array:
    if i != None:
        tmp_array.append(i) 

print(len(tmp_array))
for i in tmp_array:
    print(i)
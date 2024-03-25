n = int(input())

array = [0] * 101

for _ in range(n):
    location, alpha = input().split()
    location = int(location)
    array[location] = alpha

result = 0
for i in range(len(array)):
    cnt_G = 0
    cnt_H = 0

    if array[i] == 'G':
        cnt_G += 1
        for j in range(i + 1, len(array)):
            if array[j] == 'G':
                cnt_G += 1
                if cnt_G == cnt_H:
                    result = max(result, j - i)
                    
            elif array[j] == 'H':
                cnt_H += 1
                if cnt_G == cnt_H:
                    result = max(result, j - i)
                    

    elif array[i] == 'H':
        cnt_H += 1
        for j in range(i + 1, len(array)):
            if array[j] == 'G':
                cnt_G += 1
                if cnt_G == cnt_H:
                    result = max(result, j - i)
                    

            elif array[j] == 'H':
                cnt_H += 1
                if cnt_G == cnt_H:
                    result = max(result, j - i)
                    
            

print(result)
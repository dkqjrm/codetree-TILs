k, n = map(int, input().split())

# 1 이상 k 이하의 숫자 고르는 행위를 N번 반복하여 나올 수 있는 서로 다른 순서쌍
# 연속하여 같은 숫자가 3번 이상 나오는 경우는 제외합니다.

answer = []

def print_answer():
    for elem in answer:
        print(elem, end=' ')
    print()

def choose(curr_num):
    if curr_num == n + 1:
        print_answer()
        return
    
    for num in range(1, k+1):
        if curr_num == 1 or curr_num == 2 or not (answer[-2] == answer[-1] == num):
            answer.append(num)
            choose(curr_num + 1)
            answer.pop()

    return

choose(1)
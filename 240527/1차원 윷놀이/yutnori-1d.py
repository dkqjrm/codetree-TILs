n, m, k = map(int, input().split())
array = list(map(int, input().split()))

# 1번부터 m번까지 번호 순서대로 연결되어 있는 1차원 윷놀이 판
# k개의 말이 1번 지점에 놓여있고, n번의 턴에 숫자가 주어지고 각 턴마다 하나의 말을 선택하여 앞으로 나아갈 수 있음.
# 말은 앞으로 나아갈 때 한 칸 단위로 움직이며, 이때 앞으로 나아가던 말이 m번에 도달하면 1점을 얻게 된다.
answer = []
max_score = 0

def solve(curr_num):
    global max_score

    if curr_num == n + 1:
        score = 0
        people = [0] * k
        for idx, i in enumerate(answer):
            people[i] += array[idx]
            if people[i] >= m - 1:
                score += 1
                people[i] = -1e9
        max_score = max(max_score, score)

        return

    for num in range(0, k):
        answer.append(num)
        solve(curr_num + 1)
        answer.pop()

solve(1)
print(max_score)
A, B, x, y = map(int, input().split())

first_distance = abs(A - B) # A -> B로 간 경우
second_distance = abs(A - x) + abs(y - B) # A -> x -> y -> B로 간 경우
third_distance = abs(A - y) + abs(x - B)

print(min(first_distance, second_distance, third_distance))
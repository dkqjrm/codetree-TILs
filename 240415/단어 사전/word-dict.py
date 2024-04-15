sentence = input().split()
sentence.sort()
for i in set(sentence):
    print(i, end=' ')
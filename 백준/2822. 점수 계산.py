# 백준 2822 점수 계산
scores = []
for i in range(1,9):
    scores.append((i,int(input())))

scores.sort(key=lambda x:x[1])
scores = scores[-5:]
result = 0
for i in range(5):
    result += scores[i][1]
print(result)

scores.sort(key=lambda x:x[0])
for i in range(5):
    print(scores[i][0], end=' ')

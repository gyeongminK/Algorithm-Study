# 백준 9076 점수 집계
T = int(input())
for _ in range(T):
    scores = list(map(int, input().split()))
    scores.sort()
    scores.pop(0)
    scores.pop(-1)
    if scores[-1]-scores[0] >=4:
        print("KIN")
    else:
        print(sum(scores))

# 25. 실패율
# https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
	num = len(stages)
	stages.sort()

	result = []
	for i in range(1, N+1):
		count = 0
		while stages[0] == i:
			stages.pop(0)
			count += 1
		result.append((i, count/(len(stages)+count)))

	result.sort(key=lambda x: (-x[1], x[0]))

	answer = []
	for i in range(N):
		answer.append(result[i][0])

	return answer

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))

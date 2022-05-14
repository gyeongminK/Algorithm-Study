# 모험가 길드

n = int(input())
nums = list(map(int, input().split()))
count = 0
member = 0
nums.sort()

for num in nums:
	member +=1
	if member >= num:
		count+=1
		member = 0

print(count)

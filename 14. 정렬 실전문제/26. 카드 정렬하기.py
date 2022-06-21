# 26. 카드 정렬하기
n = int(input())
nums = []
for _ in range(n):
	nums.append(int(input()))

nums.sort()

if n==1:
	print(nums[0])
elif n ==2:
	print(nums[0]+nums[1])
else:
	sum = nums[0]+nums[1]
	for i in range(2, n):
		sum += nums[i]
	print(sum)

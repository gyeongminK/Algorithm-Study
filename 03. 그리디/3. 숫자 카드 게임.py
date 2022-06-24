# 3. 숫자 카드 게임
n,m = map(int, input().split())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

min_nums = []
for i in range(n):
    min_nums.append(min(nums[i]))

print(max(min_nums))

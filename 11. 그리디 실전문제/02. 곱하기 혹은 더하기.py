# 곱하기 혹은 더하기
s = list(input())
sum = 0
for i in range(1,len(s)):
	if s[i] == '0' or s[i-1] == '0':
		sum += int(s[i])
	else:
		sum *= int(s[i])

print(sum)

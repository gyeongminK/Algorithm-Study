# 럭키 스트레이트

n = list(input())
mid = len(n)//2
n1 = n[:mid]
n2 = n[mid:]
sum1, sum2 = 0, 0

for n in n1:
	sum1 += int(n)

for n in n2:
	sum2 += int(n)

if sum1 == sum2:
	print("LUCKY")
else:
	print("READY")
  
  

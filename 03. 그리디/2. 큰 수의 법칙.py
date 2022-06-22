# 2. 큰 수의 법칙
n, m, k = map(int, input().split()) #배열 크기, 더해지는 횟수, 연속 횟수
nums = list(map(int, input().split()))

nums.sort()

max_num = (m//k)*k
second_num = m%k

sum = nums[-1]*max_num + nums[-2]*second_num
print(sum)


# 가장 큰 수가 더해지는 횟수 공식: m//(k+1)*k + m%(k+1)

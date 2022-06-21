# 24. 안테나
n = int(input())
houses = list(map(int, input().split()))
houses.sort()
# 거리가 최솟값 -> 중간값일 때 성립
mid = (n-1)//2
print(houses[mid])

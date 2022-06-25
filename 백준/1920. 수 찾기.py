# 백준 1920 수 찾기
n = int(input())
a = list(map(int, input().split()))
m = int(input())
nums = list(map(int,input().split()))

a.sort()

def binary_search(a, k):
    start = 0
    end = len(a)-1
    while start<=end:
        mid = (start + end) // 2
        if a[mid] > k:
            end = mid - 1
        elif a[mid] < k:
            start = mid + 1
        else:
            return 1
    return 0

for num in nums:
    print(binary_search(a, num))

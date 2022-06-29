# 백준 2748 피보나치 수

# DP
def fibo(n):
    d = [0] * 91
    d[1]= 1
    d[2]= 1

    for i in range(3, n+1):
        d[i] = d[i-1]+d[i-2]

    return d[n]

n  = int(input())
print(pibo(n))

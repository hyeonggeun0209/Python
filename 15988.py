from sys import stdin
M = int(stdin.readline())
dp = [1,2,4,7]
for i in range(M):
    n = int(stdin.readline())
    for j in range(len(dp), n):
        dp.append((dp[-3]+dp[-2]+dp[-1])%1000000009)
    print(dp[n-1])
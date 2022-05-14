from sys import stdin
n = int(stdin.readline())
dp = list([])
dp.append([0,1])
for j in range(n):
    a = int(dp[j][0] + dp[j][1])
    b = int(dp[j][0])
    dp.append([a,b])
print(dp[n-1][0] + dp[n-1][1])

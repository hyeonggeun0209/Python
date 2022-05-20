from sys import stdin

n = int(stdin.readline())

dp = list()
dp.append(1)
dp.append(2)
# print(dp[0])
for i in range(2,n):
    dp.append((dp[i-2] + dp[i-1]) % 10007)

print(dp[n-1])


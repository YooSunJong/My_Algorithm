# 1로 만들기

import sys
n = int(sys.stdin.readline().rstrip())
dp = [0]*1000001
dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(4, n+1):
    if i%3 == 0:
        if dp[i] == 0:
            dp[i] = dp[i//3] + 1
        else:
            dp[i] = min(dp[i], dp[i//3] + 1)
    if i%2 == 0:
        if dp[i] == 0:
            dp[i] = dp[i//2] + 1
        else:
            dp[i] = min(dp[i], dp[i//2] + 1)
    if dp[i] == 0:
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = min(dp[i], dp[i-1] + 1)
print(dp[n])

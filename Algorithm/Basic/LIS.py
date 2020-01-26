

"""
Longest Increasing Subsequence
가장 긴 증가하는 부분수열
"""

n = int(input())

a = list(map(int, input().split()))
dp = [0]*n

dp[0] = 1


for i in range(1, len(a)):
    min = 0
    for j in range(i):
        
        if a[j] < a[i]:
            if min < dp[j]:
                min=dp[j]
    dp[i] = min+1

print(max(dp))
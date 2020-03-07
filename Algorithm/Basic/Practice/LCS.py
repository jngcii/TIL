

"""
Longest Common Subsequence
가장 긴 공통 부분수열
"""

a, b = input().split()
print(a, b)

c = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            c[i][j] = c[i-1][j-1]+1
        else:
            c[i][j] = max(c[i-1][j], c[i][j-1])

print(c[-1][-1])
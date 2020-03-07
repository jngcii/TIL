# 다시풀기.... 강의 다시듣기

n, k = map(int, input().split())

a = [0]+list(map(int, input().split()))
s = [0]*(n+1)

for i in range(1, n+1):
    s[i] = s[i-1] + a[i]

for i in range(1, n+1):
    for j in range(n):

# A[i] + ... + A[j] == k 인 (i, j) 쌍의 개수를 찾는 문제이다.
# S[j] - S[i-1] == k 인 (i, j) 쌍의 개수를 찾는 문제와 같다.
# 각각의 j에 대해서, i-1의 개수를 빠르게 찾으면 된다.
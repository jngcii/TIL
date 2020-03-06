# Fenwick Tree

###### 2020.03.06

- RMQ에서 Segment Tree를 대신해서 사요할 수 있는 트리
- RMQ는 최소를 구하는것인데 Segment Tree는 최소, 최대, 합을 모두 구할수 있다.
- Fenwick Tree는 합을 구하는데만 사용할 수 있는 트리.

### 누적합
- 수열 A[1], A[2], ..., A[N]이 있을 때, A[i] + ... + A[j]를 구하는 문제
- S[i] = A[1] + A[2] + ... + A[i]
- 누적합 소스코드
    ```python
    n, m = map(int, input().split())
    a = [0]*(n+1)
    s = [0]*(n+1)
    for i in range(1, n+1):
        a[i] = int(input())
        s[i] = s[i-1] + a[i]

    while m:
        x, y = map(int, input().split())
        print(s[y]-s[x-1])
    ```
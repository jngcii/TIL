# DAG 및 위상정렬

###### 2020.02.24

- 사이클이 없는 방향 그래프

- 선행관계를 나타낼 때 자주 사용

- 사용 가능 알고리즘 : 위상정렬

### 위상 정렬

- 그래프의 간선 u -> v 가 u가 v보다 먼저라는 의미일 때 정점의 순서를 찾는 알고리즘

- BFS 를 이용하여 풀 수 있다. 제일 중요한 것은 in-degree(어떤 정점에 들어오는 간선의 갯수가 몇개인지)

- 어떤 정점이 큐에 추가되는 것은 in-degree가 0일때

- 큐에 가장 먼저 들어 있는 것은 들어오는 간선의 갯수가 0인 것이다.

- BFS를 이용한 방법
  
    ```python
    from collections import deque

    q = deque()

    # ind[i] = i의 in-degree

    # 시작해 놓기
    for i in range(n):
        if ind[i] == 0:
            q.append(i)


    while q:
        p = q.popleft()

        print(p)

        for ai in a[p]:
            
            ind[ai] -= 1

            if ind[ai] == 0:
                q.append(ai)
    ```
> 시간복잡도는 BFS와 같은 O(E) : 모든 간선의 갯수

- DFS를 이용한 방법

    - 그래프의 간선을 모두 뒤집어 놓고 DFS를 수행하고 정점이 스택에서 빠져나오는 순서를 기록하면 위상 정렬의 순서와 같다.
    - 해당 정점을 빠진다는 의미는 그 정점에서 갈 수 있는 곳은 모두 갔다는 의미이기 때문이다.

    ```python
    def go(x):
        check[x] = True;

        for xi in a[x]:
            if not check[xi]:
                go(xi)
        
        print(x)
    ```
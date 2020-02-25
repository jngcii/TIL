# MST

###### 2020.02.25

- **M**inimum **S**panning **T**ree

- 스패닝 트리 : 그래프에서 일부 간선을 선택해서 만든 트리

- 최소 스패닝 트리 : 스패닝 트리 중에서 선택한 간선의 가중치의 합이 최소인 트리


## MST를 찾는 두가지 알고리즘

> 두 알고리즘에서 제울 즁요한 것은 사이클을 만들지 않는것
> 
> 트리는 사이클이 없기 때문

### I. Prim

1. 그래프에서 아무 정점이나 선택한다.
2. 선택한 정점과 선택하지 않은 정점을 연결하는 간선 중에 최소값을 고른다. 이 간선은 (u, v) 라고 한다. (u: 선택, v: 선택하지 않음)
3. 선택한 간선을 MST에 추가하고, v를 선택한다.
4. 모든 정점을 선택하지 않았다면, 2번 단계로 돌아간다.

- 하나를 고르고, 그다음 한개씩 선택 정점으로 옮기는 과정으로 v-1번을 반복
- 이 과정은 한번당, 모든 간선 중 선택-선택x을 찾고 그 중 최소를 찾아야 한다.
- 각각의 정점을 선택하고 모든 간선을 살펴봐야 한다.
- 시간 복잡도 : O(V X E) 최대 O(V^3)

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

<br />

### II. Kruscal
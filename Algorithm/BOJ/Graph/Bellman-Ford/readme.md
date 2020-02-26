# 최단 경로

###### 2020. 02.26

- 시작점이 1개일 때, 다른 모든 곳으로 가는 최단 경로 구하기
- **임의의 정점 A에서 B로 가는 최단 경로는 최대 V-1개의 간선으로 이루어져 있다.**

### Bellman-Ford 알고리즘

> 모든 간선 e (from, to, cost)에 대해서 다음을 검사한다. <br />
> dist[to] = min(dist[to], dist[from] + cost)

- from(시작점)에서 to(끝점)까지 가는 비용을 cost라고 하자
- dist[i]는 시작점에서 정점 i 까지 가는 최단 경로를 기록한 것
- if dist[to] > dist[from] + cost   ; to까지 가는 거리보다 from 에서 지금의 간선을 이용해 가는게 더 빠르면
- dist[to] = dist[from] + cost   ; 그 때의 to까지 가는 거리는 from까지 간다음에 cost를 더하는 그 값
- 지금까지의 식은 간선 1개에 대한 검사이기 때문에 이것을 n-1번 검사하는 것이 Bellman-Ford알고리즘이다.
<br />
- 시간 복잡도 : O(VE)
- E <= V^2 이기 때문에 O(V^3)
- 가중치가 음수가 있는 경우에도 사용할 수 있다.
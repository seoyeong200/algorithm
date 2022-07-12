## 다익스트라 알고리즘

![img](./다익스트라.png)

- 단일출발점에서 최단경로를 구하는 알고리즘
- 노드와 가중치를 가진 간선으로 graph 자료구조 사용
- 선택된 노드 중 가장 가까운 노드를 저장하는 배열, 해당 노드로의 최단거리 배열 을 업데이트 해나감
- heapQueue를 사용한다.

### 알고리즘
    1. 출발 노드 & 도착 노드 설정하고, 거리 값 부여해서 dijkstra() 호출
    2. 출발 노드에서 시작해서 방문하지 않은 인접 노드를 방문 & 거리 계산
       1. 현재 저장된 거리보다 짧으면 해당 값으로 업데이트
    3. 현재 노드에 인접한 모든 미방문 노드들까지 거리 다 계산했으면 현재 노드는 미방문 집합에서 제거
    4. 도착 노드가 미방문 노드 집합에서 제거되면 종료

### 자료구조
- 방문하지 않은 인접 노드를 방문하는 부분을 `우선순위 큐`로 구현한다.
- 지금까지 발견된 가장 가까운(distance 최솟값) 노드에 대해 먼저 계산할 수 있음
- 더 긴 거리로 계산되면 스킵
- heapq 모듈 사용
  
<span style="font-size:85%">

```python
import heapq  # 우선순위 큐 구현을 위함


def dijkstra(graph, start):
  # start로 부터의 거리 값을 저장하기 위함
  distances = {node: float('inf') for node in graph}  
  distances[start] = 0  # 시작 값은 0이어야 함
  queue = []
  # 시작 노드부터 탐색 시작 하기 위함.
  heapq.heappush(queue, [distances[start], start])  

  while queue:  # queue에 남아 있는 노드가 없으면 끝
    # 탐색 할 노드, 거리를 가져옴.
    current_distance, current_destination = heapq.heappop(queue)  

    # 기존에 있는 거리보다 길다면, 볼 필요도 없음
    if distances[current_destination] < current_distance:  
      continue
    
    for new_destination, new_distance in graph[current_destination].items():
      # 해당 노드를 거쳐 갈 때 거리
      distance = current_distance + new_distance  
      # 알고 있는 거리 보다 작으면 갱신
      if distance < distances[new_destination]:  
        distances[new_destination] = distance
        # 다음 인접 거리를 계산 하기 위해 큐에 삽입
        heapq.heappush(queue, [distance, new_destination])  
    
  return distances
```
</span>


<백준>
18513 샘터
20444 색종이와 가위
2115 갤러리

<프로그래머스>
https://school.programmers.co.kr/learn/courses/30/lessons/68645

<해커랭크> 
https://www.hackerrank.com/challenges/binary-search-tree-1/problem?isFullScreen=true

### 너비우선탐색
: Queue

<span style=80%>

```python
def bfs(graph, input_start):
    answer = []; visited = [False] * len(graph)
    queue = [input_start]; visited[input_start] = True

    while queue:
        node = queue.pop()
        answer.append(node)
        for i in range(len(graph[node])):
            if graph[node][i] == 1 and not visited[i] and node!=i:
                queue.append(i)
                visited[i] = True
    return answer

```
</span>
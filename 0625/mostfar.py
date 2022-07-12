# n = int(input()) # 땅 후보의 개수
# a, b, c = map(int, input().split()) # land 중 하나에 살고있음
# m = int(input()) # 땅 사이를 잇는 도로 개수
'''
a, b, c를 제외한 나머지 land 에서 a, b, c 각각 까지의 거리를 heapq에 넣어주면서 
    - 최소보다 더 작으먼 pop하는걸 기본으로 잡고
1. 모든 조합의 땅-땅 배열 만들고 house_candidate * friends 조합 다 돌면서 계속 최솟값 업데이트
    - 아니나다를까 시간초과남 당연함
2. floyd 나 dijkstra 알고리즘 사용해야할 것 같다.

'''
def first(n, m, a, b, c):
    land = {}

    for i in range(1, n+1):
        for j in range(i+1, n+1):
            land[(i, j)] = -1 # 메모리 초과날것같음

    for _ in range(m):
        landD, landE, roadL = map(int, input().split())
        land[(landD, landE)] = roadL # 딕셔너리 이용


    friends = list(set([a, b, c]))
    house_candidate = [i for i in range(1, n+1) if i not in friends]

    each_distance = {}
    for h in house_candidate:
        d = 10001
        for f in friends:
            if h<f and land[(h, f)] >= 0 and land[(h, f)] < d:
                d = land[(h, f)]
            elif h>f and land[(f, h)] >= 0 and land[(f, h)] <d:
                d = land[(f, h)]
        each_distance[h] = d
    # print(each_distance)

    distance_sort = sorted(each_distance.items(), key=lambda x: x[1], reverse=True)
    print(distance_sort[0][0])

########################################
from heapq import heappop, heappush
def dijkstra(graph, start):
    print(start)
    # INT_MAX = int(10e9)
    distance = [10001] * len(graph)
    distance[start] = 0
    heap = [[0, start]]
    while heap:
        print(distance, heap)
        dist, node = heappop(heap)
        print("dist: ", dist, "node: ", node)
        if distance[node] != dist: 
            print("distance[node] != dist -> stop")
            continue
        for next_node, next_dist in graph[node]:
            if dist + next_dist < distance[next_node]:
                distance[next_node] = dist + next_dist
                print("update distance")
                heappush(heap, [distance[next_node], next_node])
                print(distance, heap)
 
    return distance

def second():
    n = int(input()) # 땅 후보의 개수
    a, b, c = map(int, input().split()) # land 중 하나에 살고있음
    m = int(input()) # 땅 사이를 잇는 도로 개수

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        D, E, L = map(int, input().split())
        graph[D].append([E, L])
        graph[E].append([D, L])
    # graph : [[], [[2, 1], [4, 2], [6, 5]], 
    # [[1, 1], [3, 4], [5, 3]], 
    # [[2, 4], [4, 2]], 
    # [[1, 2], [3, 2], [5, 6]], 
    # [[2, 3], [6, 2], [4, 6]], 
    # [[1, 5], [5, 2]]]

    max_size = 0
    answer = 0
    dist_a = dijkstra(graph, a)
    dist_b = dijkstra(graph, b)
    dist_c = dijkstra(graph, c)
    
    for i in range(1, n+1):
        if max_size < min(dist_a[i], dist_b[i], dist_c[i]):
            max_size = min(dist_a[i], dist_b[i], dist_c[i])
            answer = i
            
    print(answer)

second()
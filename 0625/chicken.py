from itertools import combinations
def chickenDistance(distance):
    total = 0
    for d in distance:
        total+=min(d)
    return total

n, m = map(int, input().split())
citymap = []
for i in range(n):
    tmp = input().split(" ")
    citymap.append(tmp)
    
# 치킨집, 집들의 위치(인덱스) 구하기
chicken = []
house = []
for i in range(n):
    for j in range(n):
        if citymap[i][j] == '2':
            chicken.append((i, j))
        elif citymap[i][j] == '1':
            house.append((i, j))
# print(chicken, "\n", house)
# [(0, 1), (3, 0), (4, 0), (4, 1), (4, 4)] 
# [(0, 3), (1, 0), (1, 2), (3, 3), (3, 4), (4, 3)]

# 치킨 - 집 거리 모두 나타내는 배열 계산
distance = []
house_chickenD = 0
for h in house:
    chickenD_min=999; tmp = []
    for c in chicken:
        d = abs(h[0]-c[0])+abs(h[1]-c[1])
        tmp.append(d)
        if chickenD_min > d:
            chickenD_min = d
    distance.append(tmp)
    house_chickenD += chickenD_min
# print(distance)
# [[2, 6, 7, 6, 5], [2, 2, 3, 4, 7], [2, 4, 5, 4, 5], [5, 3, 4, 3, 2], [6, 4, 5, 4, 1], [6, 4, 3, 2, 1]]
# print(house_chickenD) 10 : 치킨집 제거 안해도 될 때 도시치킨거리

if len(chicken)==m: # m==치킨집수 면 제거 안해도 되니까 도시치킨거리 그대로 리턴
    answer = house_chickenD 
else: # 아니면 m개 선택해서(조합) 각 경우에서의 도시치킨거리 구하면서 계속 최솟값 업데이트
    combin = list(combinations([i for i in range(len(distance)-1)], m))
    answer = 999
    for com in combin: #(0, 1), (0, 2), ...
        remained_chicken = []
        for i in range(len(distance)):
            remained_chicken.append([distance[i][c] for c in com])
        
        dist = chickenDistance(remained_chicken)
        # print(com, remained_chicken, dist)
        if answer > dist:
            answer = dist
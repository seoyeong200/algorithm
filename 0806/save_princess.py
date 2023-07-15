## revise in branch-test1

def rescue():
    cache[1][0][0] = 1 # (0,0) 첫 장소 방문표시
    q = [] # bfs용 큐
    q.append([0, 0, 0, False]) # 용사 처음 상태 push - (0,0) 처음 위치니까 0초, 검 없음
    while len(q)!=0:
        # print(q)
        # 현재 상태
        current_State = q.pop(0)
        curY = current_State[0]; curX = current_State[1]; curTime = current_State[2]; curHave = current_State[3]
        for i in range(4): # 4가지 방향으로 이동하는 경우에 대해
            # 다음 상태 계산
            nextY = curY + dy[i]; nextX = curX + dx[i]
            nextTime = curTime + 1
            if nextY>=0 and nextY<n and nextX>=0 and nextX<m: # 성 벗어났는지 검사
                # 그람이 부술 수 있는 벽의 개수 제한 없음 ! -> 이 부분 
                if curHave or castle[nextY][nextX]==2:
                    nextHave = True
                else:
                    nextHave = False
                # print("next", nextY, nextX)
                # 공주 구했으면 return
                if nextY == m-1 and nextX == n-1:
                    return nextTime
                # 아니면 이동
                if curHave or castle[nextY][nextX]!=1: # 검 갖고있거나 벽이 아닌지 검사
                    if cache[1][nextY][nextX] == 0: # 이미 지나온 길인지 검사 (아직 안지나갔으면 0)
                        q.append([nextY, nextX, nextTime, nextHave])
                        cache[0][nextY][nextX] = nextTime
                        cache[1][nextY][nextX] = 1
    return -1

# n, m, t = 6, 6, 16
# castle = [[0, 0, 0, 0, 1, 1],
# [0, 0, 0, 0, 0, 2],
# [1, 1, 1, 0, 1, 0],
# [0, 0, 0, 0, 0, 0],
# [0, 1, 1, 1, 1, 1],
# [0, 0, 0, 0, 0, 0]]
n, m, t = map(int, input().split())
castle = []
for _ in range(n):
    tmp = input().split()
    castle.append(tmp)
# cache[y][x][검 유무] = 검 유무, (y, x) 처음 방문했을 때 시간
cache = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(2)]
#(cache)
# [
#     [[0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0]], 

#     [[0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0], 
#     [0, 0, 0, 0, 0, 0]]
# ]
dy = [0, 0, 1, -1]
dx = [1, -1, 0, 0]

result = rescue()
if result == -1:
    print("Fail")
else:
    print(result)








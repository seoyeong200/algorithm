from functools import reduce # first()

n, k = map(int, input().split())
lake = list(map(int, input().split()))
n = 2; k = 5; lake = [0, 3]

def first(n, k, lake): # 시간초과
    house = []
    location = lake
    idx = 1; distance = []
    while True:
        for i in range(n):
            house_candidate = lake[i]+idx
            if house_candidate not in location and len(house) <= k:
                house.append(house_candidate)
                location.append(house_candidate)
                distance.append(idx)

            house_candidate = lake[i]-idx
            if house_candidate not in location and len(house) <= k:
                house.append(house_candidate)
                location.append(house_candidate)
                distance.append(idx)

            if len(house) == k:
                break

        if len(house) == k:
            # house.pop(-1); distance.pop(-1)
            break
        idx+=1
    print(reduce(lambda x, y:x+y,distance))

def second(n, k, lake): # bfs, 이것도 시간초과 ^^
    que = []; visit = []
    for i in lake:
        que.append((i, 1)) # (샘터위치, 불행도) 저장, 불행도 초기값 1
        visit.append(i)

    answer = 0 # 전체 불행도
    house_num = 0
    while que:
        # print(que)
        now_loc, unhappy = que.pop(0)
        for d in [1, -1]:
            new_loc = now_loc+d
            if new_loc not in visit:
                visit.append(new_loc)
                que.append((new_loc, unhappy+1))
                answer += unhappy
                house_num+=1
                # print(answer, house_num)

            if house_num == k:
                que = []
                break

    print(answer)


second(n, k, lake)
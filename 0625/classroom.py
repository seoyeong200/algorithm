from heapq import heappush, heappop


def get_input():
    n = int(input())
    schedule = []
    for _ in range(n):
        _, start, end = map(int, input().split(" "))
        schedule.append((start, end))
    return n, schedule

def myanswer():
    n = 8
    schedule = [(15, 21), (20, 25), (3, 8), (2, 14), (6, 27), (7, 13), (12, 18), (6, 20)]
    classroom = 1
    class_end_times = [-1]
    schedule = sorted(schedule, key=lambda x: x[0])

    for i in schedule:
        class_end_times.sort()
        
        if i[0] < class_end_times[0]:
            classroom+=1
            class_end_times.append(i[1])
        else:
            class_end_times[0] = i[1]
        # print(i, class_end_times, classroom)

    print(classroom)
'''
가장 작은 원소가 [0] 자리에 위치하는 heapq 자료구조를 사용해서
- heapq : 시작시간이 가장 빠른 순서대로 강의 시간을 반환하는 힙큐
- q : 현재 진행중인 강의(가장 끝나는 시간이 빠른 강의가 맨 앞에 위치한 자료구조) 
    -> 끝나는 시간 < 시적시간 이면 해당 end time pop해서 강의 진행 중에서 빼주고
        새로 시작한 강의 end time push 해줘서 진행중에 넣어주기

'''

def revisew_heapq():
    n = int(input())
    heap = []; q = []
    for _ in range(n):
        _, start, end = map(int, input().split(" "))
        heappush(heap, (start, end))
        
    start, end = heappop(heap) 
    heappush(q, end)

    while heap:
        start, end = heappop(heap)
        if start >= q[0]: # 가장 일찍 끝날 강의보다 시작시간이 더 뒤쪽이면 timetable에 배정
            heappop(q)
        heappush(q, end)

    print(len(q))

    

revisew_heapq()


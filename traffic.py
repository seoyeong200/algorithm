import math
import datetime
def solution(lines):
    answer = 0
    start_end = set()
    
    for l in lines:
        end = datetime.datetime.strptime(l.split(" ")[0]+" "+l.split(" ")[1], "%Y-%m-%d %H:%M:%S.%f") # date까지 포함
        during = datetime.timedelta(seconds=float(l.split(" ")[2][:-1]))
        start = end - during + datetime.timedelta(seconds=0.001)
        # end = datetime.datetime.time(end)
        # start = datetime.datetime.time(start)
        # start_end['start'].append(start)
        # start_end['end'].append(end)
        start_end |= set([(start, end)])
    
    max_th = 0
    for i, (x_start, x_end) in enumerate(start_end):
        print(i,"번쩨 log")
        throughput = 0
        # x_start 기준 처리량 계산
        print(datetime.datetime.time(x_start) ,"기준 처리량 계산"); idx=0
        for start, end in start_end:
            if start <= x_start:
                if (start <= x_start and end >= x_start) or (start>=x_start and start <= x_start+datetime.timedelta(seconds=1)):
                    throughput+=1
                    print("process ", idx, datetime.datetime.time(start), datetime.datetime.time(end), throughput)
            idx+=1
        if max_th < throughput:
            max_th = throughput
        throughput=0
        # x_end 기준 처리량 계산
        print(datetime.datetime.time(x_end) ,"기준 처리량 계산"); idx=0
        for start, end in start_end:
            x = x_end-datetime.timedelta(seconds=1)
            if start <= x_end:
                if (start <= x and end >= x) or (start>=x and start <= x_end):
                    throughput+=1
                    print("process ", idx, datetime.datetime.time(start), datetime.datetime.time(end), throughput)
            idx+=1
        if max_th < throughput:
            max_th = throughput
                
        
    return max_th

print("------ans6------")
ans6 = solution(["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"])
print(ans6)
print("------ans5-----")
ans5 = solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"])
print(ans5)
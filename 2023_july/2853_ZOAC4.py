'''
H W N M 이 주어졌을 때 강의실에 수용할 수 있는 인원의 최댓값 구하기
 H * W 강의실
 |참가자 x 행 번호 - 참자가 y 행 번호| > N 
 or
 |참자가 x 열 번호 - 참가자 y 열 번호 | > M

 
[i][j] 에 앉은 경우 
[i+1]...[i+n]
[j+1]...[j+m] 공석
n, m = 1, 2 일 경우 아래가 하나의 덩어리
    0 x x
    x x x
-> (h / (n+1) 한 값의 ceiling) * (w / (m+1) 한 값의 ceiling)

input : 5 4 1 1 
output: 6

input: 6 5 1 2
output: 8
'''

import math
h, w, n, m = map(int, input().split())
print(math.ceil(h/(n+1)) * math.ceil(w/(m+1)))








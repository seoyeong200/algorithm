## 아아악 드디어 맞았다

from functools import reduce
def p_lst(lst):
    for i in range(len(lst)):
        print(lst[i])


def solution(n):
    snail_array = [[1 for _ in range(n)] for _ in range(n)]
    first_idx = 0; val = 0
    stop_val = reduce(lambda x, y: x+y, [i for i in range(1, n+1)])
    while True:
        # print(n, first_idx)
        for i in range(first_idx, n):
            if snail_array[i][first_idx] == 1:
                snail_array[i][first_idx] += val
                val+=1
        # print("옆으로")
        for i in range(first_idx+1, n):
            if snail_array[n-1][i] == 1:
                snail_array[n-1][i] += val
                val+=1

        # print("대각선위로")
        for i in range(n-1, first_idx, -1):
            if snail_array[i][i-first_idx] == 1:
                snail_array[i][i-first_idx] += val
                val+=1
        # p_lst(snail_array)
        
        first_idx+=1; n-=1
        if val == stop_val:
            break
    
    answer = [1]
    for i in range(1, len(snail_array)):
        for j in range(len(snail_array)):
            if snail_array[i][j] > 1:
                answer.append(snail_array[i][j])
   
    return snail_array


# ans1 = solution(4) # [1, 2, 9, 3, 10, 8, 4, 5, 6, 7]
# ans2 = solution(5) # [1, 2, 12, 3, 13, 11, 4, 14, 15, 10, 5, 6, 7, 8, 9]
ans3 = solution(7) # [1, 2, 15, 3, 16, 14, 4, 17, 21, 13, 5, 18, 19, 20, 12, 6, 7, 8, 9, 10, 11]

# for i in range(4):
#     print(ans1[i])

# for i in range(5):
#     print(ans2[i])

p_lst(ans3)

n, m = map(int, input().split())
gallery=[]
for i in range(n):
    gallery.append(input())

overlape_check = {'XX..':[], '..XX':[], 'X.X.':[], '.X.X':[]}
count=0
for i in range(n-1):
    for j in range(m-1):
        check = gallery[i][j:j+2]+gallery[i+1][j:j+2]
        if check == 'XX..':
            overlape_check[check].append([(i, j), (i, j+1)])
            # overlape_check[check].append((i, j+1))

        elif check == '..XX':
            overlape_check[check].append([(i+1, j), (i+1, j+1)])
            # overlape_check[check].append((i+1, j+1))
        elif check == 'X.X.':
            overlape_check[check].append([(i, j), (i+1, j)])
            # overlape_check[check].append((i+1, j))
        elif check == '.X.X':
            overlape_check[check].append([(i, j+1), (i+1, j+1)])
            # overlape_check[check].append((i+1, j+1))


# print(count)
# print(overlape_check)

answer = []
count=0
for i in overlape_check.keys():
    # print(overlape_check[i])
    tmp=[]
    # count+=(len(set(overlape_check[i])))//2
    for j in range(len(overlape_check[i])):
        if overlape_check[i][j][0] not in tmp and overlape_check[i][j][1] not in tmp:
            tmp.append(overlape_check[i][j][0])
            tmp.append(overlape_check[i][j][1])
    count += len(tmp)//2


'''
{'XX..': [[(0, 5), (0, 6)], 
        [(0, 6), (0, 7)],  #
        [(0, 7), (0, 8)]], 
'..XX': [[(2, 6), (2, 7)], 
        [(4, 2), (4, 3)], 
        [(6, 1), (6, 2)], 
        [(6, 5), (6, 6)], 
        [(6, 6), (6, 7)]], #
'X.X.': [[(1, 2), (2, 2)], 
        [(1, 4), (2, 4)], 
        [(2, 7), (3, 7)], 
        [(4, 0), (5, 0)]], 
'.X.X': [[(1, 4), (2, 4)], 
        [(1, 9), (2, 9)], 
        [(2, 6), (3, 6)], 
        [(2, 9), (3, 9)],  #
        [(3, 6), (4, 6)], 
        [(3, 9), (4, 9)]]} #
'''

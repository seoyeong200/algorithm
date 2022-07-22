n, k = map(int, input().split())

def first():
    variation =[]
    if n%2 == 0:
        for i in range(n//2+1):
            variation.append((i+1) * (n-i+1))

    else:
        for i in range((n-1)//2+1):
            variation.append((i+1) * (n-i+1))

    if k in variation:
        print("YEs")
    else:
        print("NO")

'''
냅다 하니까 시간초과났다.
계속 두개로 나눠서 k가 나오는지 확인하는 방식으로 풀어야될듯, 이분탐색
위에서 풀었던거 이용해서 풀면될듯 ?!(재귀로)

'''
def divide(n, left, right, k):
    # print(f"divide({left}, {right})")
    if left <= right: # 탐색 실패 = k는 색종이를 잘라서 만들 수 없는 경우
        return "NO"

    amount = left - right + 1
    if amount % 2 == 0:
        mid = left-(amount//2+1)
    else:
        mid = left-(amount//2)
    print(mid)
    if (mid+1) * (n-mid+1) == k or (mid+2) * (n-mid+2) == k:
        return "YES"
    else:
        divide(n, left, mid, k)
        divide(n, mid-1, right, k)
    
# answer = divide(n, n, n//2, k)
# print(answer)

def answer(n, k):
    left=0
    right=n//2
    possible = False

    while left <= right:
        rowcut = (left+right) // 2 # n=4면 (0+2)//2=1
        colcut = n - rowcut
        pieces = (rowcut+1) * (colcut+1)
        if k == pieces:
            print("YES"); possible=True
            break
        if k > pieces:
            left = rowcut+1
        else:
            right = rowcut-1

    if not possible:
        print("NO")

answer(n, k)
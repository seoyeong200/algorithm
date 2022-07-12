n, k = map(int, input().split())
coin = []
for _ in range(n):
    c = int(input())
    coin.append(c)

dp = [0 for _ in range(k+1)]

dp[0]=1

for i, c in enumerate(coin):
    for j in range(1, k+1):
        if c <= j:
            dp[j] += dp[j-c]
    print(dp)

print(dp[k])








c, n = map(int, input().split())
ad_effect = [list(map(int, input().split())) for _ in range(n)]

dp = [0]+[10001]*(c+100)
print(dp)

for cost, customer in ad_effect:
    for i in range(customer, c+101):
        dp[i] = min(dp[i], dp[i-customer]+cost)
        print(dp)

print(min(dp[c:c+101]))
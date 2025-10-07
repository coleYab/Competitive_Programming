# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

n = int(input())
a = list(map(int, input().split()))
dp = [float("inf")] * (n+1)
dp[0] = 0

for i in range(1, n):
  dp[i] = min(dp[i], abs(a[i] - a[i - 1]) + dp[i - 1])
  if i > 1:
    dp[i] = min(dp[i], abs(a[i] - a[i - 2]) + dp[i - 2])

print(dp[n - 1])
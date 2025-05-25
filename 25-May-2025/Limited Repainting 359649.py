# Problem: Limited Repainting - https://codeforces.com/contest/2070/problem/C

def solve():
    n, m = map(int, input().split())
    s = input()
    p = list(map(int, input().split()))

    puns = []
    left = 0
    cur = 0
    for right in range(n):
        if s[right] != s[left]:
            puns.append((s[left], cur))
            left = right 
            cur = 0
        cur = max(p[right], cur)
        if right == n - 1:
            puns.append((s[right], cur))
    
    def check(mid):
        cnt = 0
        left = 0
        while left < len(puns) and puns[left][0] == "R":
            left += 1
        N = len(puns)
        for i in range(left, N):
            if i == left and (puns[i][0] == "R" or puns[i][1] <= mid):
                left = i + 1
                continue
        
            if i == N - 1 or (puns[i][0] == "R" and puns[i][1] > mid and left != i):
                cnt += 1
                left = i + 1
                continue

        return cnt <= m

    ans = 0
    left, right = 0, 1 << 100
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    print(ans)

tt = int(input())
for i in range(tt):
    solve()
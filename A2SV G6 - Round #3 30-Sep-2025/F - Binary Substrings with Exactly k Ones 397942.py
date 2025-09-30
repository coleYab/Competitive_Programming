# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

n = int(input())
s = input()
hm = {0: 1}

cnt = 0
ans = 0
for right in range(len(s)):
    cnt += int(s[right])
    ans += hm.get(cnt - n, 0)
    hm[cnt] = hm.get(cnt, 0) + 1

print(ans)
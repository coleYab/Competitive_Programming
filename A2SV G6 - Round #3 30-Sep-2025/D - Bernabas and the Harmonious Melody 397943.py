# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

def solve():
    n = int(input())
    s = input()

    # find the first differing character and try to remove them both
    left = 0
    right = n - 1

    def validate(s, l, r, ch):
        ans = 0

        while l < r:
            if s[l] != s[r]:
                if s[l] == ch:
                    l += 1
                    ans += 1
                    continue
                    
                if s[r] == ch:
                    r -= 1
                    ans += 1
                    continue
                
                return -1
            else:
                l += 1
                r -= 1

        return ans

    ans = 0
    while left < right:
        if s[left] != s[right]:
            one = validate(s, left +1, right, s[left])
            two = validate(s, left, right - 1, s[right])
            if one == two and one == -1:
                print(-1)
            elif one == -1:
                print(two + 1)
            elif two == -1:
                print(one + 1)
            else:
                print(1 + min(one, two))
            return
        left += 1
        right -= 1
    
    print(ans)


for _ in range(int(input())):
    solve()
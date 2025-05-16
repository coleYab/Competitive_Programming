# Problem: Cirno's Perfect Bitmasks Classroom - https://codeforces.com/problemset/problem/1688/A

    n = int(input())
    ans = (n ^ (n & (n - 1)))
    if n.bit_count() == 1:
        ans |= 1 if n != 1 else (1 << 1)
    print(ans)
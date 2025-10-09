# Problem: Complicated GCD - https://codeforces.com/contest/664/problem/A

from math import gcd
a, b = map(str, input().split())
if a == b:
    print(a)
else:
    print(1)
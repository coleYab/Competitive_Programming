# Problem: Selection of Personnel - https://codeforces.com/problemset/problem/630/F


def solve():
    n = int(input())

    def comb(n, m):
        if m < 0 or m > n:
            return 0
        m = min(m, n - m)
        res = 1
        for i in range(1, m + 1):
            res = res * (n - i + 1) // i
        return res


    print(comb(n, 5) + comb(n, 6) + comb(n, 7))

solve()

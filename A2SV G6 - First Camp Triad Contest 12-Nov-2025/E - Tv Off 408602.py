# Problem: E - Tv Off - https://codeforces.com/gym/589822/problem/E

import sys, threading, time
from random import *
from math import ceil, log2, log10, remainder, gcd
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations


inf = float('inf')
mod = 10 ** 9 + 7

def add(x, y):
    rs = (x + y) % mod
    rs += mod
    return rs % mod

def mul(x, y):
    return (x * y) % mod

def inv(x):
    return pow(x, mod - 2, mod)

def div(x, y):
    p = inv(x)
    return mul(x, p)

# factorization thingsa
mxn = int(1e5+100)
facts = [1] * (mxn)
ifacts = [1] * mxn
def init():
    facts[0] = 1
    for i in range(1, mxn):
        facts[i] = mul(facts[i - 1], i)

    ifacts[mxn - 1] = inv(facts[mxn - 1])
    for i in range(mxn - 2, -1, -1):
        ifacts[i] = mul(ifacts[i + 1], i + 1)

def choose(n, r):
    if r < 0 or r > n:
        return 0
    return mul(facts[n], mul(ifacts[r], ifacts[n - r]))

HASHER = getrandbits(61)
class diction:
    def __init__(self):
        self.dic = dict()

    def __xor(self, val):
        return (HASHER ^ val)

    def set(self, key, val):
        self.dic[self.__xor(key)] = val

    def get(self, key):
        return self.dic.get(self.__xor(key), None)

    def __getitem__(self, key):
        return self.dic.get(key)

    def __setitem__(self, key, val):
        self.set(key, val)

def li(): return list(map(int, input().split()))
def mi(): return map(int, input().split())
def ii(): return int(input())
def si(): return input()

import sys
from bisect import bisect_left
input = sys.stdin.readline

class SegTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (4 * n)

    def build(self, a, v, tl, tr):
        if tl == tr:
            self.tree[v] = a[tl]
        else:
            tm = (tl + tr) // 2
            self.build(a, v * 2, tl, tm)
            self.build(a, v * 2 + 1, tm + 1, tr)
            self.tree[v] = min(self.tree[v * 2], self.tree[v * 2 + 1])

    def query(self, v, tl, tr, l, r):
        if l > r:
            return float('inf')
        if l == tl and r == tr:
            return self.tree[v]
        tm = (tl + tr) // 2
        return min(
            self.query(v * 2, tl, tm, l, min(r, tm)),
            self.query(v * 2 + 1, tm + 1, tr, max(l, tm + 1), r)
        )

def solve():
    n = int(input())
    segs = []
    coords = []

    for i in range(n):
        l, r = map(int, input().split())
        segs.append((l, r, i + 1))
        coords.append(l)
        coords.append(r + 1)

    coords = sorted(set(coords))
    m = len(coords)
    def get_idx(x):
        return bisect_left(coords, x)

    diff = [0] * (m + 2)

    for l, r, _ in segs:
        L = get_idx(l)
        R = get_idx(r + 1)
        diff[L] += 1
        diff[R] -= 1

    cover = [0] * m
    cover[0] = diff[0]
    for i in range(1, m):
        cover[i] = cover[i - 1] + diff[i]

    st = SegTree(m)
    st.build(cover, 1, 0, m - 1)

    for l, r, idx in segs:
        L = get_idx(l)
        R = get_idx(r + 1) - 1
        if st.query(1, 0, m - 1, L, R) >= 2:
            print(idx)
            return

    print(-1)

def main():
    t = 1
    # t = int(input())
    for i in range(t):
        solve()

if __name__ == "__main__":
    main()

    # sys.setrecursionlimit(1 << 30)
    # threading.stack_size(1 << 27)
    # main_thread = threading.Thread(target=main)
    # main_thread.start()
    # main_thread.join()



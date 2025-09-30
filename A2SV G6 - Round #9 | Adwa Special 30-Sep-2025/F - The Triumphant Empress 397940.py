# Problem: F - The Triumphant Empress - https://codeforces.com/gym/601269/problem/F

import sys, threading
import time
from math import ceil, log2, log10, remainder
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations

def li(): return list(map(int, input().split()))
def mi(): return map(int, input().split())

INF = float('inf')
MOD = 10 ** 9 + 7

key = (1 << 50) - 1

class diction:
    def __init__(self):
        self.dic = dict()
    
    def __xor(self, val):
        # /return val
        return (key ^ val)

    def set(self, key, val):
        self.dic[self.__xor(key)] = val

    def get(self, key):
        return self.dic.get(self.__xor(key), None)

class seg_tree:
    def __init__(self, size):
        self.size = 1
        while self.size < size: 
            self.size *= 2
        self.tree = [0] * (self.size * 2)

    def _set(self, idx, val, x, lx, rx):
        if rx - lx == 1:
            self.tree[x] += val
            return
        
        m = (lx + rx) // 2
        if idx < m:
            self._set(idx, val, 2 * x + 1, lx, m)
        else:
            self._set(idx, val, 2 * x + 2, m, rx)
        
        self.tree[x] = self.tree[2 * x + 1] + self.tree[2 * x + 2]

    def set(self, idx, val):
        self._set(idx, val, 0, 0, self.size)

    def _get(self, l, r, x, lx, rx):
        if lx >= r or l >= rx: return 0
        if l <= lx and rx <= r: return self.tree[x]
        m = (lx + rx) // 2
        return self._get(l, r, 2 * x + 1, lx, m) + self._get(l, r, 2 * x + 2, m, rx)

    def get(self, left, right):
        return self._get(left, right, 0, 0, self.size)

def solve():
    n,q = map(int,input().split())
    a = list(map(int, input().split()))
    qry = [tuple(map(int, input().split())) for i in range(q)]
    vals = []
    for i in a:
        vals.append(i)
    qry2 = []
    idx = 0
    for k, v in qry:
        vals.append(v)
        qry2.append((k, v, idx))
        idx += 1
    
    qry2.sort()
    ans = [0] * q
    vals = list(set(vals))
    vals.sort()
    dic = diction()
    for i, v in enumerate(vals):
        dic.set(v, i)
    
    # print(qry2)
    st = seg_tree(len(vals))
    cur = 0
    for i in range(q):
        k, v, idx = qry2[i]

        while cur < k and cur < len(a):
            st.set(dic.get(a[cur]), 1)
            cur += 1

        vidx = dic.get(v)
        # print("vidx = ", vidx)
        ans[idx] = st.get(0, dic.get(v))

    print(*ans, sep="\n")

def main():
    t = 1
    t = int(input())
    for i in range(t):
        solve()


if __name__ == "__main__":
    main()

#     # recursive things
#     # sys.setrecursionlimit(1 << 30)
#     # threading.stack_size(1 << 27)
#     # main_thread = threading.Thread(target=main)
#     # main_thread.start()
#     # main_thread.join()
# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

"""
 * Author: Yeabsira Moges(nba_yeabsira)
"""
import sys
import time
from math import ceil, log2, log10, remainder
from bisect import bisect_left as bl, bisect_right as br
from collections import defaultdict, deque, Counter
from heapq import heappush, heappop, heapify
from itertools import permutations, combinations
from typing import * # for leetcode 


INF = float('inf')
MOD = 10 ** 9 + 7

class DSU:
    """
    implement: dsu here and add all the varation needed
    """
    def __init__(self, cap):
        self.parent = [-1 for i in range(cap + 1)]

    def union(self, s1, s2):
        p1 = self.find(s1)
        p2 = self.find(s2)

        if p1 == p2:
            return

        tot = self.parent[p1] + self.parent[p2]
        self.parent[p2] = p1
        self.parent[p1] = tot

    def find(self, node):
        vis = []
        while self.parent[node] >= 0:
            vis.append(node)
            node = self.parent[node]
        for ch in vis:
            self.parent[ch] = node
        return node



class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        mails = {}
        mail_list = []
        owners = []
        cnt = 0
        for mail in accounts:
            owner = mail[0]
            for i in range(1, len(mail)):
                if mail[i] not in mails:
                    mails[mail[i]] = cnt 
                    mail_list.append(mail[i])
                    owners.append(owner)
                    cnt += 1

        dsu = DSU(cnt)
        for j, mail in enumerate(accounts):
            mail = mail[1:]
            for i in range(len(mail)):
                next = (i + 1) % len(mail)
                dsu.union(mails[mail[i]], mails[mail[next]])

        ans = []
        par = defaultdict(list)
        for i, v in enumerate(dsu.parent):
            if i >= len(mail_list):
                continue
        
            p = dsu.find(i)
            par[p].append(mail_list[i])

        for u,v in par.items():
            ans.append([owners[u]] + sorted(v))

        return ans


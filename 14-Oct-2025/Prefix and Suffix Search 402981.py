# Problem: Prefix and Suffix Search - https://leetcode.com/problems/prefix-and-suffix-search/


class TrieNode:
    def __init__(self):
        self.chs = [None for i in range(26)]
        self.idx = float("-inf")
        self.end = False
        self.suffix = SuffixTrie()

def get_idx(c):
    return ord(c) - ord('a')

class PrefixTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, idx):
        rt = self.root
        n = len(word)
        for i, v in enumerate(word):
            c = get_idx(v)
            if not rt.chs[c]:
                rt.chs[c] = TrieNode()
            rt.suffix.insert(word, idx)
            rt = rt.chs[c]
        rt.suffix.insert(word, idx)
        rt.end = True

    def search(self, pref, suff):
        rt = self.root
        n = len(pref)
        for i, v in enumerate(pref):
            c = get_idx(v)
            if not rt.chs[c]:
                return -1
            rt = rt.chs[c]

        if not rt:
            return -1    

        return rt.suffix.search(suff)

class Nd:
    def __init__(self):
        self.chs = [None for i in range(26)]
        self.idx = float("-inf")
    
    def __re__(self):
        return f"{self.chs} idx = {self.idx}"

class SuffixTrie:
    def __init__(self):
        self.root = Nd()        

    def insert(self, word, idx):
        word = word[::-1]
        rt = self.root
        for i, v in enumerate(word):
            c = get_idx(v)
            if not rt.chs[c]:
                rt.chs[c] = Nd()
            rt.idx = max(rt.idx, idx)
            rt = rt.chs[c]
        rt.idx = max(rt.idx, idx)
        rt.end = True

    def search(self, word):
        word = word[::-1]
        rt = self.root
        for i, v in enumerate(word):
            c = get_idx(v)
            if not rt.chs[c]:
                return -1
            rt = rt.chs[c]
        if not rt:
            return -1
        return rt.idx


class WordFilter:
    def __init__(self, words: List[str]):
        self.trie = PrefixTrie()
        for i, v in enumerate(words):
            self.trie.insert(v, i)
            
    def f(self, pref: str, suff: str) -> int:
        return self.trie.search(pref, suff)


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
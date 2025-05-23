# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def valid(path):
            if len(path) != 4:
                return False
            for a in path:
                if not a: return False
                if not 255 >= int(a) >= 0 or (a[0] == '0' and len(a) > 1):
                    return False
            return True 

        def dfs(idx, path):
            if idx >= len(s):
                if valid(path):
                    ans.append(".".join(path))
                return     

            if len(path) > 4:
                return
        
            for i in range(idx, min(len(s), idx + 3)):
                path.append(s[idx:i + 1])
                dfs(i + 1, path)
                path.pop()

        dfs(0, [])
        return ans
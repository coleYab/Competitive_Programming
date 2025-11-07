# Problem: Number of Laser Beams in a Bank - https://leetcode.com/problems/number-of-laser-beams-in-a-bank/

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        grid = []
        for i in bank:
            if i.count('1') == 0:
                continue
            grid.append(i)
        
        n = len(grid)
        for i in range(1, n):
            prev = grid[i -1].count('1')
            cur_one = grid[i].count('1')
            ans += (prev * cur_one)

        return ans 
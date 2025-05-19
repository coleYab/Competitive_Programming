# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(1 << len(nums)):
            cur = []
            for j,v  in enumerate(bin(i)[2:][::-1]):
                if v == '1':
                    cur.append(nums[j])
    
            ans.append(cur)
        
        return ans
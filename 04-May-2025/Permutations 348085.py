# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def perm(nums):
            ans = []
            if (len(nums) == 1):
                return [list(nums)]

            for i in range(len(nums)):
                top = nums.popleft()
                temp = perm(nums)
                for t in temp:
                    t.append(top)
                nums.append(top)
                ans.extend(temp)
            return ans

        dq = deque()
        for n in nums:
            dq.append(n)

        return perm(dq)
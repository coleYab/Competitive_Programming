# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-1 * p for p in piles]
        heapify(heap)
        
        for i in range(k):
            top = heappop(heap)
            heappush(heap, (-1 * (ceil((-1 * top) / 2))))

        return sum(heap) * (-1)


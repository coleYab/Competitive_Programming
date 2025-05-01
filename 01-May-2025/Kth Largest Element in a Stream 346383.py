# Problem: Kth Largest Element in a Stream - https://leetcode.com/problems/kth-largest-element-in-a-stream/

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapify(self.heap) 
        self.cap = k 
        self.scores = set(nums)      

    def add(self, val: int) -> int:

        heappush(self.heap, val)
        while len(self.heap) > self.cap:
            heappop(self.heap)
        self.scores.add(val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums[:k]
        self.k = k
        heapq.heapify(self.minheap)
        
        if len(nums) > k:
            for n in nums[k:]:
                if self.minheap[0] < n:
                    heapq.heappushpop(self.minheap, n)

    def add(self, val: int) -> int:
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
        elif val > self.minheap[0]:
            heapq.heappushpop(self.minheap, val)
        return self.minheap[0]

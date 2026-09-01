import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_heap = nums[:k]
        heapq.heapify(k_heap)
        for n in nums[k:]:
            # if n is larger than the min
            if n > k_heap[0]:
                heapq.heappushpop(k_heap, n)
        return k_heap[0]


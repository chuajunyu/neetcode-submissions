import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        result = heapq.nlargest(k, nums)
        return result[-1]
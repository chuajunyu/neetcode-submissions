class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequency of each element: O(n)
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # sort O(nlogn).
        c = list(count.items())
        c.sort(key=lambda x: -x[1])

        return [x[0] for x in c[:k]]

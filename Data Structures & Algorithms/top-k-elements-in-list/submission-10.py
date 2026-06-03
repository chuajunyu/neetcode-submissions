class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count frequency of each element: O(n)
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        # iterate through and pick top k using quickselect
        # but lazy to code quickselect LOL

        # use counting sort
        buckets = [None] * len(nums)
        for n in count:
            i = count[n] - 1
            if buckets[i] is None:
                buckets[i] = [n]
            else:
                buckets[i].append(n)

        # iterate through the buckets until we hit k
        top_k = []
        for i in range(len(nums) - 1, -1, -1):
            if buckets[i] is None:
                continue
            top_k.extend(buckets[i])
            if len(top_k) == k:
                return top_k

